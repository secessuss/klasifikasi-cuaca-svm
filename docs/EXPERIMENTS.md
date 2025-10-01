# Eksperimen & Optimisasi

Dokumen ini membandingkan dua pendekatan eksperimental:  
1. **Model Baseline (tanpa optimisasi)**  
2. **Model Optimal (dengan optimisasi)**  

---

## Eksperimen 1: Model Baseline (Tanpa Optimisasi)

**Tujuan:** Menjadi titik awal untuk mengukur performa dasar.  

### Desain Eksperimen
- **Data:** Dataset asli tanpa augmentasi (~898 gambar latih).  
- **Pipeline:** `StandardScaler + SVM`.  
- **Fitur:** Vektor gabungan **8370 dimensi** langsung dimasukkan ke SVM.  
- **Tuning:** `GridSearchCV` untuk parameter **C** dan **gamma**.  

### Hasil Baseline
- **Akurasi pada Data Uji:** **42.2%**  

### Analisis Kegagalan
- **Overfitting Parah** → model terlalu menghafal data latih.  
- **Curse of Dimensionality** → jumlah fitur (8370) >> jumlah sampel latih (~898).  
- **Bias kelas mayoritas** → performa hampir sama dengan tebakan acak (25%).  

---

## Eksperimen 2: Model Optimal (Dengan Optimisasi)

**Tujuan:** Memperbaiki kelemahan baseline dengan augmentasi data & reduksi dimensi.  

### Desain Eksperimen
- **Data Augmentation:**  
  Jumlah data latih ditingkatkan dari ~898 → **3593 gambar** (horizontal flip & perubahan kecerahan).  
  → Membantu generalisasi model.  

- **Reduksi Dimensi (PCA):**  
  Mengurangi dimensi fitur dari **8370** → lebih kecil, sambil mempertahankan **95% varians**.  
  → Mengatasi *curse of dimensionality*.  

- **Pipeline Terintegrasi:**  
  `StandardScaler + PCA + SVM`  

### Hyperparameter Tuning
- **Metode:** `GridSearchCV` dengan parameter grid yang sama.  
- **Parameter diuji:**  
  - `C`: [1, 10, 50, 100]  
  - `gamma`: [0.01, 0.001, 0.005, 0.0001]  
- **Hasil terbaik:**  
  - **C = 1**, **gamma = 0.01**  
  - **Skor validasi silang:** 93.24%  

### Hasil Optimal
- **Akurasi pada Data Uji:** **95.88%**  

---

## Kesimpulan Eksperimen
- Akurasi meningkat dari **42.2% → 95.9%** setelah optimisasi.  
- **Data Augmentation** → membuat model lebih robust terhadap variasi data.  
- **PCA** → langkah krusial untuk mengatasi *curse of dimensionality*.  
- Pipeline yang **terstruktur & optimal** lebih penting daripada hanya memilih algoritma kuat.  

---