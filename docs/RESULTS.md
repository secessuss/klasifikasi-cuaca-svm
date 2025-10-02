# Hasil Akhir

Hasil kuantitatif dari **model klasifikasi cuaca**, dievaluasi pada **225 gambar uji**.

---

## Performa Keseluruhan

Model optimal (**Data Augmentation + PCA + SVM**) mencapai performa tinggi dan seimbang di semua metrik.

| Metrik                                | Nilai   |
|---------------------------------------|---------|
| **Akurasi Keseluruhan (Data Uji)**    | 85.33%  |
| **Skor F1 Rata-rata (Macro Avg)**     | 0.84    |
| **Skor F1 Rata-rata (Weighted Avg)**  | 0.85    |
| **Parameter Terbaik (C, γ)**          | (1, 0.01) |
| **Skor Validasi Silang (CV)**         | 81.90%  |

---

## Laporan Klasifikasi Detail

| Kelas    | Precision | Recall | F1-Score | Support |
|----------|-----------|--------|----------|---------|
| Cloudy   | 0.84      | 0.90   | 0.87     | 60      |
| Rain     | 0.74      | 0.98   | 0.84     | 43      |
| Shine    | 0.87      | 0.66   | 0.75     | 50      |
| Sunrise  | 0.95      | 0.88   | 0.91     | 72      |
| **Total / Accuracy** | — | — | **0.85** | **225** |
| **Macro Avg** | 0.85 | 0.85 | 0.84 | 225 |
| **Weighted Avg** | 0.86 | 0.85 | 0.85 | 225 |

---

## Analisis

- **Recall Tinggi untuk Hujan (Rain)** → Model sangat baik dalam mengidentifikasi semua kasus hujan **(98%)**, meskipun presisinya lebih rendah. 
- **Precision Rendah untuk Hujan (Rain)** → Terdapat beberapa kasus di mana model memprediksi Hujan, padahal sebenarnya bukan.
- **Tantangan pada Kelas Cerah (Shine)** → Recall untuk kelas Shine **(66%)** adalah yang terendah, menunjukkan model kesulitan mengidentifikasi beberapa gambar cerah dengan benar.
- **Performa Kuat pada Matahari Terbit (Sunrise)** → Kelas ini memiliki F1-Score tertinggi **(0.91)**, menunjukkan keseimbangan yang baik antara presisi dan recall.

---

## Confusion Matrix

- **Diagonal Dominan** → Sebagian besar prediksi masih tepat sasaran.
- **Potensi Kebingungan** → Perlu dianalisis lebih lanjut pada matriks kebingungan untuk melihat kelas mana yang sering tertukar, terutama untuk kelas *Shine*.

---

## Analisis Error (Potensi Peningkatan)

Walaupun performa sangat tinggi, kesalahan kecil tetap ada, terutama pada kasus gambar yang **ambiguous**:  
- **Mendung sangat gelap** → mirip kondisi hujan.  
- **Matahari terbit dengan awan tipis** → bisa mirip dengan kelas *Cloudy*.  

**Peluang perbaikan:**  
- Menambahkan lebih banyak data pada kelas dengan performa rendah seperti Shine.
- Melakukan analisis error untuk memahami mengapa gambar Shine sering salah diklasifikasikan.
- Eksperimen lebih lanjut dengan teknik augmentasi atau ekstraksi fitur yang berbeda.

---