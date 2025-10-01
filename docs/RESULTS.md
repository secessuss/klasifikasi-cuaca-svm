# Hasil Akhir

Hasil kuantitatif dari **model klasifikasi cuaca**, dievaluasi pada **899 gambar uji**.

---

## Performa Keseluruhan

Model optimal (**Data Augmentation + PCA + SVM**) mencapai performa tinggi dan seimbang di semua metrik.

| Metrik                                | Nilai   |
|---------------------------------------|---------|
| **Akurasi Keseluruhan (Data Uji)**    | 95.88%  |
| **Skor F1 Rata-rata (Macro Avg)**     | 0.96    |
| **Skor F1 Rata-rata (Weighted Avg)**  | 0.96    |
| **Parameter Terbaik (C, γ)**          | (1, 0.01) |
| **Skor Validasi Silang (CV)**         | 93.24%  |

---

## Laporan Klasifikasi Detail

| Kelas    | Precision | Recall | F1-Score | Support |
|----------|-----------|--------|----------|---------|
| Cloudy   | 0.95      | 0.97   | 0.96     | 240     |
| Rain     | 0.94      | 0.98   | 0.96     | 171     |
| Shine    | 0.96      | 0.92   | 0.94     | 202     |
| Sunrise  | 0.98      | 0.97   | 0.97     | 286     |
| **Total / Accuracy** | — | — | **0.96** | **899** |
| **Macro Avg** | 0.96 | 0.96 | 0.96 | 899 |
| **Weighted Avg** | 0.96 | 0.96 | 0.96 | 899 |

---

## Analisis

- **Precision Tinggi** → Prediksi yang benar sangat konsisten (misalnya, *Sunrise* dengan precision 98%).  
- **Recall Tinggi** → Sebagian besar sampel benar terklasifikasi (misalnya, *Rain* dengan recall 98%).  
- **F1-Score Seimbang** → Skor konsisten antar kelas, tidak ada bias signifikan.  

---

## Confusion Matrix

- **Diagonal Dominan** → Mayoritas prediksi tepat.  
- **Kesalahan Kecil** → Hanya beberapa kasus *Cloudy* salah diklasifikasikan.  
- **Tidak Ada Kebingungan Sistematis** → Tidak ada pasangan kelas yang selalu tertukar.  

---

## Analisis Error (Potensi Peningkatan)

Walaupun performa sangat tinggi, kesalahan kecil tetap ada, terutama pada kasus gambar yang **ambiguous**:  
- **Mendung sangat gelap** → mirip kondisi hujan.  
- **Matahari terbit dengan awan tipis** → bisa mirip dengan kelas *Cloudy*.  

**Peluang perbaikan:**  
- Menambahkan lebih banyak data pada kasus-kasus ambigu.  
- Menggunakan teknik ekstraksi fitur yang lebih canggih (misalnya CNN-based).  

---