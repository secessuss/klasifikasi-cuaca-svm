# Gambaran Umum Proyek

Pnjelasan singkat mengenai arsitektur klasifikasi cuaca yang dibangun.

---

## Arsitektur

```mermaid
flowchart LR
    A["Input: Gambar Mentah"] --> B["Tahap 1: Prapemrosesan (Resize, Augmentasi, Konversi Warna)"]
    B --> C["Tahap 2: Ekstraksi Fitur (HOG + Color Histogram + LBP)\nVektor Fitur Dimensi Tinggi (8370)"]
    C --> D["Tahap 3: Reduksi Dimensi (PCA)\nVektor Fitur Optimal"]
    D --> E["Tahap 4: Klasifikasi (SVM dengan Kernel RBF)"]
    E --> F["Output: Label Prediksi (Cloudy, Rain, Shine, Sunrise)"]
```

---

## Ringkasan
- **Input:** Gambar mentah  
- **Prapemrosesan:** Resize, augmentasi, konversi warna  
- **Ekstraksi fitur:** HOG + Color Histogram + LBP  
- **Reduksi dimensi:** PCA  
- **Klasifikasi:** SVM dengan kernel RBF  
- **Output:** Label prediksi cuaca

---