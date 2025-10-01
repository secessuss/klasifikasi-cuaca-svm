import os
import joblib
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image

from model_wrapper import IntegratedClassifier


# Inisialisasi Aplikasi Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Muat Model
try:
    model_path = 'model/svm_model_integrated.pkl'
    model = joblib.load(model_path)
    print(f"* Model terintegrasi berhasil dimuat dari {model_path}")
except FileNotFoundError:
    print(f"* Peringatan: File model tidak ditemukan di {model_path}. Aplikasi akan gagal saat prediksi.")
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
        # Cek apakah ada file dari sesi sebelumnya dan hapus
        last_filepath = session.get('last_filepath')
        if last_filepath and os.path.exists(last_filepath):
            try:
                os.remove(last_filepath)
                print(f"* File lama '{last_filepath}' telah dihapus.")
            except Exception as e:
                print(f"* Gagal menghapus file lama: {e}")

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Simpan path file yang baru ke dalam sesi
        session['last_filepath'] = filepath

        try:
            # Buka gambar menggunakan Pillow dan konversi ke array numpy
            image = Image.open(filepath).convert('RGB') # formatnya RGB
            image_np = np.array(image)

            # Lakukan prediksi langsung pada gambar mentah
            if model:
                # Model menerima list dari gambar, bungkus dengan []
                prediction_idx = model.predict([image_np])[0]
                prediction_class = CLASSES[prediction_idx]
                
                # Dapatkan skor kepercayaan (probabilitas)
                confidence_scores = model.predict_proba([image_np])[0]
                confidence = round(confidence_scores[prediction_idx] * 100, 2)
                
                all_scores = list(zip(CLASSES, confidence_scores))
                all_confidences = sorted(
                    [(name, round(score * 100, 2)) for name, score in all_scores],
                    key=lambda item: item[1],
                    reverse=True
                )

            else:
                flash("Model tidak dapat dimuat. Prediksi tidak tersedia.")
                return redirect(url_for('index'))
            
            return render_template('result.html', 
                                   filename=filename, 
                                   prediction=prediction_class, 
                                   confidence=confidence,
                                   all_confidences=all_confidences)

        except Exception as e:
            flash(f'Terjadi kesalahan saat memproses gambar: {e}')
            return redirect(url_for('index'))

    else:
        flash('Jenis file yang diizinkan adalah png, jpg, jpeg')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
