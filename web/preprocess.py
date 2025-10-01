'''
import cv2
import numpy as np
from skimage.feature import hog, local_binary_pattern

# KONFIGURASI DARI PROYEK MACHINE LEARNING!!!
# Pastikan semua parameter ini SAMA PERSIS dengan yang digunakan saat training.
IMAGE_SIZE = (128, 128)
HOG_ORIENTATIONS = 9
HOG_PIXELS_PER_CELL = (8, 8)
HOG_CELLS_PER_BLOCK = (2, 2)
LBP_RADIUS = 8
LBP_N_POINTS = 24

def _resize_image(image):
    """Mengubah ukuran gambar."""
    return cv2.resize(image, IMAGE_SIZE, interpolation=cv2.INTER_AREA)

def _to_grayscale(image):
    """Mengonversi gambar menjadi grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def _normalize_image(image):
    """Normalisasi nilai piksel ke rentang [0, 1]."""
    return image.astype('float32') / 255.0

def _extract_hog_features(gray_image):
    """Mengekstrak fitur HOG."""
    return hog(
        gray_image, orientations=HOG_ORIENTATIONS, pixels_per_cell=HOG_PIXELS_PER_CELL,
        cells_per_block=HOG_CELLS_PER_BLOCK, block_norm='L2-Hys', visualize=False, transform_sqrt=True
    )

def _extract_color_histogram(color_image):
    """Mengekstrak histogram warna HSV."""
    hsv_image = cv2.cvtColor((color_image * 255).astype(np.uint8), cv2.COLOR_BGR2HSV)
    hist_h = cv2.calcHist([hsv_image], [0], None, [180], [0, 180])
    hist_s = cv2.calcHist([hsv_image], [1], None, [32], [0, 256])
    hist_v = cv2.calcHist([hsv_image], [2], None, [32], [0, 256])
    cv2.normalize(hist_h, hist_h)
    cv2.normalize(hist_s, hist_s)
    cv2.normalize(hist_v, hist_v)
    return np.concatenate((hist_h, hist_s, hist_v)).flatten()

def _extract_lbp_features(gray_image):
    """Mengekstrak fitur LBP."""
    gray_image_uint8 = (gray_image * 255).astype(np.uint8)
    lbp = local_binary_pattern(gray_image_uint8, LBP_N_POINTS, LBP_RADIUS, method='uniform')
    (hist, _) = np.histogram(lbp.ravel(), bins=np.arange(0, LBP_N_POINTS + 3), range=(0, LBP_N_POINTS + 2))
    hist = hist.astype("float")
    hist /= (hist.sum() + 1e-6)
    return hist

def preprocess_image_for_prediction(image_np):
    """
    Pipeline lengkap untuk memproses satu gambar dari array numpy (hasil upload)
    dan mengekstrak fitur gabungannya, siap untuk prediksi model.
    Penting: Pillow (Flask) membaca sebagai RGB, OpenCV bekerja dengan BGR.
    """
    # 1. Konversi dari RGB (Pillow) ke BGR (OpenCV)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # 2. Resize gambar berwarna
    resized_color = _resize_image(image_bgr)
    
    # 3. Konversi ke grayscale untuk HOG dan LBP
    gray_image = _to_grayscale(resized_color)
    
    # 4. Normalisasi keduanya
    normalized_gray = _normalize_image(gray_image)
    normalized_color = _normalize_image(resized_color)

    # 5. Ekstraksi Fitur
    hog_features = _extract_hog_features(normalized_gray)
    color_hist_features = _extract_color_histogram(normalized_color)
    lbp_features = _extract_lbp_features(normalized_gray)

    # 6. Gabungkan semua fitur menjadi satu vektor
    combined_features = np.hstack([hog_features, color_hist_features, lbp_features])
    
    return combined_features
'''