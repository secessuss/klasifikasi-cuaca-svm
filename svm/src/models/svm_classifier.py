# Definisi, training, dan penggunaan model SVM

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
import joblib
from src.config import SAVED_MODEL_PATH

def create_svm_pipeline_with_pca():
    """
    Pipeline yang terdiri dari scaler, PCA untuk reduksi dimensi, dan classifier SVM.
    """
    pipeline = make_pipeline(
        StandardScaler(),
        # n_components=0.95 berarti PCA akan memilih
        # jumlah komponen yang cukup untuk menjelaskan 95% varians data.
        PCA(n_components=0.95, random_state=42),
        SVC(kernel='rbf', probability=True, random_state=42, class_weight='balanced')
    )
    return pipeline

def tune_and_train_model(X_train, y_train):
    """
    Melakukan tuning hyperparameter menggunakan GridSearchCV dan melatih model.
    Sekarang menggunakan pipeline dengan PCA.
    """
    # Gunakan pipeline baru yang sudah ada PCA di dalamnya
    pipeline = create_svm_pipeline_with_pca()

    # Bisa sedikit sesuaikan grid search karena PCA mengubah ruang fitur
    # 'svc__' masih digunakan karena nama step dalam pipeline adalah 'svc'
    param_grid = {
        'svc__C': [1, 10, 50, 100],
        'svc__gamma': [0.01, 0.001, 0.005, 0.0001],
    }

    print("="*50)
    print("MEMULAI EKSEKUSI DENGAN PCA DAN GRID SEARCH BARU")
    print(f"Parameter Grid yang Diuji: {param_grid}")
    print("="*50)

    print("Memulai tuning hyperparameter dengan GridSearchCV...")
    grid_search = GridSearchCV(pipeline, param_grid, cv=3, verbose=2)
    grid_search.fit(X_train, y_train)

    print("\nTuning selesai.")
    print(f"Parameter terbaik ditemukan: {grid_search.best_params_}")
    print(f"Skor cross-validation terbaik: {grid_search.best_score_:.4f}")

    # Cetak jumlah komponen PCA yang dipilih
    if hasattr(grid_search.best_estimator_.named_steps['pca'], 'n_components_'):
        n_components = grid_search.best_estimator_.named_steps['pca'].n_components_
        print(f"PCA memilih {n_components} komponen.")

    return grid_search.best_estimator_

def save_model(model):
    """
    Menyimpan model yang telah dilatih ke file.
    """
    joblib.dump(model, SAVED_MODEL_PATH)
    print(f"Model berhasil disimpan di {SAVED_MODEL_PATH}")

def load_model():
    """
    Memuat model dari file.
    """
    if SAVED_MODEL_PATH:
        model = joblib.load(SAVED_MODEL_PATH)
        print(f"Model berhasil dimuat dari {SAVED_MODEL_PATH}")
        return model
    else:
        raise FileNotFoundError("Path model tidak ditemukan.")
