## Panduan Teknis Penggunaan Proyek

Instruksi langkah demi langkah untuk menyiapkan lingkungan, melatih model dari awal, dan melakukan prediksi pada gambar baru.

---

### Prasyarat

* Python **3.8** atau lebih baru sudah terinstal di sistem Anda.

---

### Pengaturan Lingkungan

#### 1. Clone Repositori (Jika belum)

```bash
git clone https://github.com/secessuss/klasifikasi-cuaca-svm.git
cd klasifikasi-cuaca-svm
```

#### 2. Buat Lingkungan Virtual (Direkomendasikan)

```bash
python -m venv venv
```

Aktifkan lingkungan virtual:

* **Windows**

  ```bash
  venv\Scripts\activate
  ```
* **macOS/Linux**

  ```bash
  source venv/bin/activate
  ```

> **Catatan**: Lingkungan virtual ini digunakan untuk **seluruh project**, mencakup proses **training model** di folder `svm/` maupun **menjalankan aplikasi web** di folder `web/`.

#### 3. Instal Dependensi

```bash
pip install -r requirements.txt
```

Library utama:
`scikit-learn`, `opencv-python-headless`, `numpy`, `scikit-image`, `matplotlib`, `joblib`.

---

### Cara Melatih Model (Training)

1. Pastikan dataset tersedia di:

   ```
   svm/data/raw/
   ```

2. Buka terminal, masuk ke folder `svm/`:

   ```bash
   cd svm
   ```

3. Jalankan pipeline training:

   ```bash
   python run.py
   ```

Setelah selesai, tiga output utama akan tersimpan:

* **Model** → `svm/saved_models/svm_model.pkl`
* **Laporan klasifikasi** → `svm/experiments/results/classification_report.txt`
* **Confusion matrix** → `svm/experiments/results/confusion_matrix.png`

---

### Cara Melakukan Prediksi pada Gambar Baru

1. Letakkan gambar baru ke folder:

   ```
   svm/data/new_images/
   ```

2. Jalankan skrip prediksi:

   * Untuk **satu gambar**:

     ```bash
     python predict.py data/new_images/nama_file_gambar.jpg
     ```
   * Untuk **seluruh folder**:

     ```bash
     python predict.py data/new_images
     ```

3. Hasil prediksi akan muncul di terminal, misalnya:

```
--- Memproses file: berawan.jpg ---
-> Prediksi: Cloudy (Kepercayaan: 94.64%)

--- Memproses file: hujan.jpg ---
-> Prediksi: Rain (Kepercayaan: 99.99%)
```

---

[Kembali ke README](../README.md)
