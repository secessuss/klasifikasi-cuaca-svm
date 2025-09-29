# File untuk menyimpan semua parameter dan konfigurasi global

import os

# PATH
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_RAW_PATH = os.path.join(BASE_DIR, '../system/data/raw') # Sesuaikan nama folder dataset jika berbeda
SAVED_MODEL_PATH = os.path.join(BASE_DIR, '../system/saved_models/svm_model.pkl')
RESULTS_PATH = os.path.join(BASE_DIR, '../system/experiments/results')

# IMAGE PREPROCESSING
IMAGE_SIZE = (128, 128) # Ukuran gambar (lebar, tinggi)

# FEATURE EXTRACTION (HOG)
HOG_ORIENTATIONS = 9
HOG_PIXELS_PER_CELL = (8, 8)
HOG_CELLS_PER_BLOCK = (2, 2)

# MODEL TRAINING
TEST_SIZE = 0.2
RANDOM_STATE = 42

# DATASET CLASSES
CLASSES = ["Cloudy", "Rain", "Shine", "Sunrise"]
