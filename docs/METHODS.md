# Metodologi Teknis

Menjelaskan secara rinci teknik-teknik yang digunakan dalam pipeline machine learning, mulai dari **ekstraksi fitur** hingga **klasifikasi**.

---

## Ekstraksi Fitur (*Feature Extraction*)

Tujuan tahap ini adalah mengubah **data piksel mentah** dari gambar menjadi **vektor fitur numerik** yang ringkas namun informatif.  
Proyek ini menggabungkan **tiga metode ekstraksi fitur klasik** untuk menangkap aspek visual yang berbeda.

### a. Histogram of Oriented Gradients (HOG)
- **Apa yang Ditangkap:** Bentuk & kontur objek.  
- **Bagaimana Caranya:** HOG menghitung distribusi arah gradien (perubahan intensitas piksel) di dalam sel-sel kecil gambar. Efektif untuk mendeteksi tepi dan kontur tanpa banyak dipengaruhi pencahayaan.  
- **Peran dalam Proyek:** Membedakan struktur langit → misalnya awan tebal (*Cloudy*) vs langit cerah (*Shine*).  

### b. Color Histogram
- **Apa yang Ditangkap:** Distribusi warna global.  
- **Bagaimana Caranya:** Histogram dihitung dalam ruang warna **HSV** (Hue, Saturation, Value) yang lebih robust terhadap pencahayaan dibanding RGB. Hue sangat membantu membedakan palet warna.  
- **Peran dalam Proyek:** Penting untuk memisahkan **Sunrise** (didominasi oranye/merah) dari **Shine** (didominasi biru).  

### c. Local Binary Patterns (LBP)
- **Apa yang Ditangkap:** Tekstur mikro.  
- **Bagaimana Caranya:** LBP membandingkan intensitas tiap piksel dengan tetangganya, menghasilkan deskriptor tekstur yang ringkas dan stabil.  
- **Peran dalam Proyek:** Mengidentifikasi tekstur halus, seperti permukaan awan lembut atau tetesan hujan.  

**Vektor Fitur Gabungan:**  
Ketiga metode digabung → menghasilkan **8370 dimensi** fitur per gambar.  

---

## Reduksi Dimensi (*Dimensionality Reduction*)

- **Masalah:** Vektor fitur berukuran **8370 dimensi** → terlalu besar → rawan *curse of dimensionality* → overfitting.  
- **Teknik:** **Principal Component Analysis (PCA)**.  
- **Bagaimana Caranya:** PCA memproyeksikan data ke koordinat baru yang memaksimalkan varians. Komponen dengan varians kecil (noise) dibuang.  
- **Implementasi:** PCA dikonfigurasi untuk mempertahankan **95% varians total** → dimensi berkurang drastis sambil menjaga informasi utama.  

---

## Model Klasifikasi

- **Algoritma:** **Support Vector Machine (SVM)**  
- **Mengapa SVM?**  
  - Sangat efektif di ruang berdimensi tinggi  
  - Mampu membentuk batas keputusan kompleks antar kelas  

### Konfigurasi SVM
- **Kernel:** `RBF` → fleksibel untuk pola non-linear pada data visual  
- **Penyeimbangan Kelas:** `class_weight='balanced'` → memberi bobot lebih besar pada kelas minoritas (misalnya *Rain*)  
- **Hyperparameter Tuning:**  
  Dilakukan dengan **GridSearchCV**, mencari kombinasi terbaik:  
  - **C (Regularisasi):** trade-off margin maksimal vs kesalahan klasifikasi  
  - **gamma:** mengatur pengaruh tiap sampel data latih  

---