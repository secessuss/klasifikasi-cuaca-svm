import os
import joblib
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image
from preprocess import preprocess_image_for_prediction

# Inisialisasi Aplikasi Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Muat Model
# Menggunakan joblib karena model scikit-learn disimpan dengannya
try:
    model_path = 'model/svm_model.pkl'
    model = joblib.load(model_path)
    print(f"* Model berhasil dimuat dari {model_path}")
except FileNotFoundError:
    print(f"* Peringatan: File model tidak ditemukan di {model_path}. Aplikasi mungkin gagal saat prediksi.")
    model = None
except Exception as e:
    print(f"* Terjadi kesalahan saat memuat model: {e}")
    model = None

# Daftar kelas sesuai dengan urutan saat training
CLASSES = ["Cloudy", "Rain", "Shine", "Sunrise"]
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    """Memeriksa apakah ekstensi file diizinkan."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Merender halaman utama."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Merender halaman tentang."""
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Menangani upload gambar dan melakukan prediksi."""
    if 'file' not in request.files:
        flash('Tidak ada bagian file')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('Tidak ada gambar yang dipilih untuk diunggah')
        return redirect(url_for('index'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            # Buka gambar menggunakan Pillow
            image = Image.open(filepath)
            # Konversi ke array numpy
            image_np = np.array(image)

            # Lakukan pra-pemrosesan
            features = preprocess_image_for_prediction(image_np)
            
            # Lakukan prediksi
            if model:
                prediction_idx = model.predict([features])[0]
                prediction_class = CLASSES[prediction_idx]
                
                # Dapatkan skor kepercayaan (probabilitas)
                confidence_scores = model.predict_proba([features])[0]
                confidence = round(confidence_scores[prediction_idx] * 100, 2)
            else:
                flash("Model tidak dapat dimuat. Prediksi tidak tersedia.")
                return redirect(url_for('index'))


            return render_template('result.html', 
                                   filename=filename, 
                                   prediction=prediction_class, 
                                   confidence=confidence)

        except Exception as e:
            flash(f'Terjadi kesalahan saat memproses gambar: {e}')
            return redirect(url_for('index'))
    else:
        flash('Jenis file yang diizinkan adalah png, jpg, jpeg')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
