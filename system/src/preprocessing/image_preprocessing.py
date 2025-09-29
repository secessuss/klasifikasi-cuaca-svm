# Fungsi-fungsi untuk prapemrosesan gambar

import cv2
import numpy as np
from src.config import IMAGE_SIZE

def resize_image(image):
    """
    Mengubah ukuran gambar ke ukuran yang telah ditentukan di config.
    """
    return cv2.resize(image, IMAGE_SIZE, interpolation=cv2.INTER_AREA)

def to_grayscale(image):
    """
    Mengonversi gambar menjadi grayscale.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def normalize_image(image):
    """
    Normalisasi nilai piksel gambar ke rentang [0, 1].
    Gambar harus dalam format float.
    """
    return image.astype('float32') / 255.0

def preprocess_image_for_feature_extraction(image):
    """
    Pipeline prapemrosesan lengkap untuk satu gambar.
    Menghasilkan gambar grayscale yang dinormalisasi dan gambar berwarna yang dinormalisasi.
    """
    # Resize gambar asli (berwarna)
    resized_color = resize_image(image)
    
    # Konversi ke grayscale
    gray_image = to_grayscale(resized_color)
    
    # Normalisasi keduanya
    normalized_gray = normalize_image(gray_image)
    normalized_color = normalize_image(resized_color)
    
    return normalized_gray, normalized_color
