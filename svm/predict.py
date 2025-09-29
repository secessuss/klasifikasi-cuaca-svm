# Skrip untuk melakukan prediksi pada gambar baru menggunakan model yang sudah dilatih

import os
import sys
import cv2
import numpy as np
import warnings

warnings.filterwarnings('ignore', category=UserWarning)
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.config import CLASSES
from src.models.svm_classifier import load_model
from src.preprocessing.image_preprocessing import preprocess_image_for_feature_extraction
from src.features.feature_extraction import extract_features

def predict_single_image(image_path, model):
    """
    Melakukan prediksi pada satu gambar tunggal.

    Args:
        image_path (str): Path lengkap ke file gambar.
        model (Pipeline): Model scikit-learn yang sudah dilatih.

    Returns:
        tuple: (kelas_prediksi, tingkat_kepercayaan) atau (None, None) jika gagal.
    """
    try:
        # 1. Baca gambar menggunakan OpenCV
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Tidak dapat membaca gambar di {image_path}")
            return None, None

        # 2. Preprocessing (langkahnya harus sama persis seperti saat training)
        gray_img, color_img = preprocess_image_for_feature_extraction(image)

        # 3. Ekstraksi Fitur (langkahnya harus sama persis seperti saat training)
        features = extract_features(gray_img, color_img)
        
        # Reshape fitur karena model mengharapkan input 2D (n_samples, n_features)
        features = features.reshape(1, -1)

        # 4. Lakukan Prediksi
        # Model pipeline sudah termasuk scaler dan PCA, jadi kita bisa langsung memanggil .predict()
        prediction_idx = model.predict(features)[0]
        predicted_class = CLASSES[prediction_idx]

        # 5. Dapatkan probabilitas untuk melihat tingkat kepercayaan (opsional tapi berguna)
        probabilities = model.predict_proba(features)[0]
        confidence = probabilities[prediction_idx]

        return predicted_class, confidence

    except Exception as e:
        print(f"Terjadi error saat memproses {image_path}: {e}")
        return None, None

def main():
    """
    Fungsi utama untuk memuat model dan memproses gambar dari argumen command line.
    """
    print("--- Memulai Sesi Prediksi Cuaca ---")

    # 1. Muat model yang sudah dilatih
    try:
        model = load_model()
    except FileNotFoundError:
        print("Error: File model 'svm_model.pkl' tidak ditemukan. Pastikan Anda sudah menjalankan pipeline training (run.py).")
        return

    # 2. Dapatkan path gambar/folder dari argumen command line
    if len(sys.argv) < 2:
        print("\nPenggunaan: python predict.py <path_ke_gambar_atau_folder>")
        print("Contoh (satu gambar): python predict.py data/new_images/test1.jpg")
        print("Contoh (satu folder): python predict.py data/new_images")
        return

    input_path = sys.argv[1]

    # 3. Proses path input
    if os.path.isfile(input_path):
        # Jika input adalah satu file gambar
        print(f"\nMemproses file tunggal: {input_path}")
        predicted_class, confidence = predict_single_image(input_path, model)
        if predicted_class:
            print(f"-> Prediksi: {predicted_class} (Kepercayaan: {confidence:.2%})")

    elif os.path.isdir(input_path):
        # Jika input adalah sebuah folder
        print(f"\nMemproses semua gambar di folder: {input_path}")
        image_files = [f for f in os.listdir(input_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
        
        if not image_files:
            print("Tidak ada file gambar (.png, .jpg, .jpeg) yang ditemukan di folder ini.")
            return
            
        for filename in image_files:
            image_path = os.path.join(input_path, filename)
            print(f"\n--- Memproses file: {filename} ---")
            predicted_class, confidence = predict_single_image(image_path, model)
            if predicted_class:
                print(f"-> Prediksi: {predicted_class} (Kepercayaan: {confidence:.2%})")

    else:
        print(f"Error: Path tidak valid -> {input_path}")
        print("Pastikan path menunjuk ke file gambar atau folder yang berisi gambar.")

if __name__ == "__main__":
    main()
