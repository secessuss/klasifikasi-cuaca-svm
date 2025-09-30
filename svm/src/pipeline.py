import os
import cv2
import numpy as np
from tqdm import tqdm
from sklearn.model_selection import train_test_split

from src.config import TEST_SIZE, RANDOM_STATE, DATA_PROCESSED_PATH, CLASSES
from src.utils.dataset_loader import load_images_from_folder
from src.preprocessing.image_preprocessing import preprocess_image_for_feature_extraction
from src.features.feature_extraction import extract_features
from src.models.svm_classifier import tune_and_train_model, save_model
from src.utils.metrics import evaluate_model, plot_confusion_matrix
from src.utils.logger import logger

def run_pipeline(data_path):
    """
    Menjalankan seluruh alur kerja: load, preprocess, feature extraction, train, evaluate.
    """
    # 1. Load Data
    images, labels, filenames = load_images_from_folder(data_path, use_augmentation=True)
    if not images:
        logger.warning("Tidak ada gambar untuk diproses. Pipeline berhenti.")
        return

    # 2. Preprocessing & Feature Extraction
    feature_list = []
    logger.info("Memulai prapemrosesan, penyimpanan gambar, dan ekstraksi fitur...")
    
    for image, label, filename in tqdm(zip(images, labels, filenames), total=len(images), desc="Processing Images"):
        # Preprocessing
        gray_img, color_img, resized_for_saving = preprocess_image_for_feature_extraction(image)
        
        # Simpan gambar yang telah diproses
        try:
            class_name = CLASSES[label]
            # Buat sub-direktori per kelas di dalam folder processed
            processed_class_dir = os.path.join(DATA_PROCESSED_PATH, class_name)
            os.makedirs(processed_class_dir, exist_ok=True)

            # Buat nama file unik untuk gambar augmentasi
            base, ext = os.path.splitext(filename)
            # Dapatkan hash dari gambar untuk membuat nama file unik jika ada augmentasi
            img_hash = abs(hash(image.tostring())) % (10 ** 8)
            save_filename = f"{base}_{img_hash}{ext}"
            save_path = os.path.join(processed_class_dir, save_filename)
            
            # Simpan gambar (resized_for_saving dalam format uint8)
            cv2.imwrite(save_path, resized_for_saving)
        except Exception as e:
            logger.error(f"Gagal menyimpan gambar yang diproses untuk {filename}: {e}")

        # Ekstraksi fitur
        features = extract_features(gray_img, color_img)
        feature_list.append(features)
    
    X = np.array(feature_list)
    y = np.array(labels)
    
    logger.info(f"Ekstraksi fitur selesai. Bentuk matriks fitur: {X.shape}")

    # 3. Split Data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )
    logger.info(f"Data dibagi: {len(X_train)} train, {len(X_test)} test.")

    # 4. Train Model
    model = tune_and_train_model(X_train, y_train)
    
    # 5. Save Model
    save_model(model)
    
    # 6. Evaluate Model
    logger.info("Mengevaluasi model pada data test...")
    y_pred = model.predict(X_test)
    
    evaluate_model(y_test, y_pred)
    plot_confusion_matrix(y_test, y_pred)