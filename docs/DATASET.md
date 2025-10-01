# Analisis dan Prapemrosesan Dataset

Merinci **sumber data, karakteristik, distribusi kelas, serta tahapan prapemrosesan** yang diterapkan pada dataset gambar cuaca.

---

## Sumber & Spesifikasi Dataset

- **Nama:** Multi-class Weather Dataset for Image Classification  
- **Sumber:** [Kaggle](https://www.kaggle.com/datasets/pratik2901/multiclass-weather-dataset)
- **Total Gambar Awal:** 1125 gambar berwarna  
- **Format:** Mayoritas `.jpg`  
- **Jumlah Kelas:** 4 kategori cuaca  
  - **Cloudy (Berawan)**  
  - **Rain (Hujan)**  
  - **Shine (Cerah/Terik)**  
  - **Sunrise (Matahari Terbit)**  

---

## Distribusi Kelas

Jumlah gambar untuk setiap kelas tidak seimbang: *Sunrise* paling banyak, *Rain* paling sedikit.

| Kelas   | Jumlah Gambar |
|---------|---------------|
| Sunrise | 357           |
| Cloudy  | 300           |
| Shine   | 253           |
| Rain    | 215           |
| **Total** | **1125**   |

**Implikasi:**  
Ketidakseimbangan kelas dapat membuat model bias.  
**Solusi:** Gunakan parameter `class_weight='balanced'` pada SVM → memberi bobot lebih besar pada kelas minoritas.

---

## Contoh Gambar per Kelas

- **Cloudy vs. Rain** → Sama-sama bernuansa abu-abu/gelap, berpotensi membingungkan model.  
- **Shine vs. Sunrise** → Dapat dibedakan lewat dominasi warna (biru cerah vs. oranye/merah).  

---

## Tahapan Prapemrosesan

### 1. Standardisasi Ukuran (*Resize*)
- **Masalah:** Gambar memiliki resolusi bervariasi.  
- **Solusi:** Semua gambar diubah ke **128×128 piksel**.  
  - Kompromi antara detail visual yang cukup & efisiensi komputasi.  

---

### 2. Augmentasi Data (*Data Augmentation*)
- **Tujuan:** Menambah jumlah & variasi data → mengurangi overfitting, meningkatkan generalisasi.  
- **Metode yang diterapkan:**
  - **Horizontal Flip** → variasi perspektif  
  - **Perubahan Kecerahan** → simulasi kondisi pencahayaan berbeda  
- **Hasil:**  
  - Data latih meningkat dari ~898 → **3593 sampel** setelah augmentasi.  

---

### 3. Pembagian Data (*Train/Test Split*)
- **Data Latih (80%)** → 3593 gambar (setelah augmentasi), digunakan untuk training & tuning.  
- **Data Uji (20%)** → 899 gambar, digunakan untuk evaluasi akhir.  
- **Metode:** Stratified split → proporsi tiap kelas tetap konsisten.

---