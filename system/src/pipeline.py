# Pipeline utama yang mengintegrasikan semua langkah

import numpy as np
from tqdm import tqdm
from sklearn.model_selection import train_test_split

from src.config import TEST_SIZE, RANDOM_STATE
from src.utils.dataset_loader import load_images_from_folder
from src.preprocessing.image_preprocessing import preprocess_image_for_feature_extraction
from src.features.feature_extraction import extract_features
from src.models.svm_classifier import tune_and_train_model, save_model
from src.utils.metrics import evaluate_model, plot_confusion_matrix

def run_pipeline(data_path):
    """
    Menjalankan seluruh alur kerja: load, preprocess, feature extraction, train, evaluate.
    """
    # 1. Load Data
    images, labels = load_images_from_folder(data_path, use_augmentation=True)
    if not images:
        print("Tidak ada gambar untuk diproses. Pipeline berhenti.")
        return

    # 2. Preprocessing & Feature Extraction
    feature_list = []
    print("\nMemulai prapemrosesan dan ekstraksi fitur...")
    for image in tqdm(images, desc="Extracting Features"):
        gray_img, color_img = preprocess_image_for_feature_extraction(image)
        features = extract_features(gray_img, color_img)
        feature_list.append(features)
    
    X = np.array(feature_list)
    y = np.array(labels)
    
    print(f"Ekstraksi fitur selesai. Bentuk matriks fitur: {X.shape}")

    # 3. Split Data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )
    print(f"Data dibagi: {len(X_train)} train, {len(X_test)} test.")

    # 4. Train Model (sekarang dengan tuning)
    model = tune_and_train_model(X_train, y_train)
    
    # 5. Save Model
    save_model(model)
    
    # 6. Evaluate Model
    print("\nMengevaluasi model pada data test...")
    y_pred = model.predict(X_test)
    
    evaluate_model(y_test, y_pred)
    plot_confusion_matrix(y_test, y_pred)

