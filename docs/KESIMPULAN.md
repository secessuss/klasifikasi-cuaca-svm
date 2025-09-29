## Kesimpulan

Membahas interpretasi dari hasil akhir, kesimpulan yang dapat ditarik dari proyek, serta untuk pengembangan.

---

### Analisis Mendalam Hasil Akhir

Model akhir (Data Augmentation + PCA + SVM) mencapai **akurasi 95.4%**, hasil yang sangat memuaskan. Keberhasilan ini ditopang oleh dua faktor utama:

#### Dampak Kritis dari PCA

* **Mengatasi Overfitting** → menghapus dimensi tidak signifikan (noise).
* **Efisiensi Komputasi** → pelatihan & tuning jauh lebih cepat (1114 fitur vs 8370 fitur).
* **Fokus pada Varians** → hanya mempertahankan fitur yang relevan untuk klasifikasi.

#### Peran Penting Data Augmentation

* **Meningkatkan Generalisasi** → model lebih tangguh menghadapi variasi data baru.
* **Menyediakan Data untuk PCA** → jumlah data yang lebih banyak membuat PCA lebih efektif.

---

### ⚠️ Potensi Kesalahan Model

Meskipun performa tinggi, model masih bisa keliru pada gambar ambigu:

* Langit mendung pekat ↔ bisa salah diklasifikasikan sebagai *Rain*.
* Sunrise yang sangat cerah ↔ bisa mirip dengan *Shine*.

Kesalahan ini wajar, karena batas visual antar kelas tidak selalu jelas.

---

### Kesimpulan Utama

1. **Kombinasi Fitur Klasik Masih Relevan**
   HOG, LBP, dan Color Histogram tetap efektif bila dikelola dengan benar.

2. **Manajemen Fitur adalah Kunci**
   Tanpa reduksi dimensi (PCA), performa model pada data berdimensi tinggi akan runtuh.

3. **Data adalah Fondasi**
   Augmentasi data terbukti menjadi cara efisien untuk memperkaya dataset.

4. **Pipeline Optimal Tercapai**
   Proyek ini berhasil membangun pipeline end-to-end yang akurat, terukur, dan andal.

---

### Pengembangan Lebih Lanjut (Kalau lagi mood)

Beberapa ide untuk pengembangan ke depan:

* **Kelas 'Lain-lain'**
  Tambahkan kelas tambahan untuk gambar non-cuaca agar sistem lebih robust.

* **Eksplorasi Deep Learning**
  Coba CNN (misalnya ResNet, MobileNet) untuk membandingkan performa dengan pendekatan klasik.

* **Deployment Model**
  Bungkus model ke dalam API sederhana (Flask/FastAPI) agar bisa digunakan sebagai layanan prediksi.

* **Analisis Fitur Lanjutan**
  Gunakan SHAP untuk memvisualisasikan bagian gambar yang paling berpengaruh terhadap prediksi model.

---

[Kembali ke README](../README.md)
