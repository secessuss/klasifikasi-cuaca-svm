import os
from src.pipeline import run_pipeline
from src.config import DATA_RAW_PATH, SAVED_MODEL_PATH, RESULTS_PATH

def main():
    """
    Fungsi utama
    """
    print("Memulai pipeline klasifikasi cuaca...")

    if not os.path.exists(SAVED_MODEL_PATH):
        os.makedirs(os.path.dirname(SAVED_MODEL_PATH), exist_ok=True)
    if not os.path.exists(RESULTS_PATH):
        os.makedirs(RESULTS_PATH, exist_ok=True)

    try:
        run_pipeline(data_path=DATA_RAW_PATH)
        print("\nPipeline selesai.")
        print(f"Model tersimpan di: {SAVED_MODEL_PATH}")
        print(f"Hasil evaluasi tersimpan di direktori: {RESULTS_PATH}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menjalankan pipeline: {e}")

if __name__ == "__main__":
    main()
