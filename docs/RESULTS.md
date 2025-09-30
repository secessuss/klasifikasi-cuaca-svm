# Desain Eksperimen dan Hasil

Untuk mencapai model klasifikasi yang optimal, saya melakukan dua eksperimen utama dan membandingkan hasilnya.

---

## Eksperimen 1: Pendekatan Awal (Baseline)

### Desain

* **Data:** Dataset asli (~1123 gambar), tanpa augmentasi
* **Prapemrosesan:** Resize, konversi warna, normalisasi
* **Ekstraksi Fitur:** HOG + Color Histogram + LBP → 8370 fitur
* **Model:** SVM + StandardScaler (tanpa PCA)
* **Tuning:** GridSearchCV untuk parameter `C` & `gamma`

### Hasil

* **Akurasi Validasi Silang (CV):** 37.3%
* **Akurasi Data Tes:** 42.2%

**Laporan Klasifikasi (Data Tes):**

```
              precision    recall  f1-score   support
      Cloudy       1.00      0.22      0.36        60
        Rain       1.00      0.09      0.17        43
       Shine       1.00      0.12      0.21        50
     Sunrise       0.36      1.00      0.53        72
```

**Confusion Matrix Awal:**
*(gambar tidak tersedia untuk baseline)*

### Analisis

* Akurasi sangat rendah (42%), nyaris seperti tebak acak (25%).
* Model bias ekstrem ke kelas **Sunrise**.
* Recall untuk **Cloudy**, **Rain**, **Shine** hampir nol.
* **Akar masalah:** *curse of dimensionality* (8370 fitur vs ~898 data latih).

---

## Eksperimen 2: PCA + Data Augmentation (Optimal)

### Desain

* **Data:** Data Augmentation → jumlah data latih ~3369 gambar
* **Prapemrosesan & Ekstraksi Fitur:** Sama (8370 fitur awal)
* **Reduksi Dimensi:** PCA (pertahankan 95% varians)
* **Model:** SVM + StandardScaler + PCA
* **Tuning:** GridSearchCV untuk `C` & `gamma`

### Hasil

* **Akurasi Validasi Silang (CV):** 91.5%
* **Akurasi Data Tes:** 96.4%
* **Reduksi Fitur:** Dari 8370 → 1114 komponen utama

**Laporan Klasifikasi (Data Tes):**

```
              precision    recall  f1-score   support
      Cloudy       0.95      0.97      0.96       240
        Rain       0.94      0.98      0.96       171
       Shine       0.98      0.93      0.95       202
     Sunrise       0.98      0.98      0.98       286

    accuracy                           0.96       899
   macro avg       0.96      0.96      0.96       899
weighted avg       0.96      0.96      0.96       899
```

**Confusion Matrix Akhir:**
![Confusion Matrix](../svm/experiments/results/confusion_matrix.png)

### Analisis

* Akurasi melonjak drastis dari **42.2% → 96.4%**
* Semua kelas seimbang: precision, recall, f1-score > 0.93
* Bias model hilang total
* PCA + Augmentasi terbukti sangat efektif untuk **generalisasi & reduksi overfitting**

---

## Perbandingan Hasil

| Metrik            | Eksperimen 1 (Baseline) | Eksperimen 2 (Optimal) | Peningkatan   |
| ----------------- | ----------------------- | ---------------------- | ------------- |
| **Akurasi Tes**   | 42.2%                   | 96.4%                  | +54.2%        |
| **Recall Rata2**  | 36%                     | 96%                    | +60%          |
| **Bias Model**    | Tinggi (Sunrise)        | Tidak Ada              | Teratasi      |
| **Dimensi Fitur** | 8370                    | 1114                   | Reduksi 86.7% |

---

[Kembali ke README](../README.md)
