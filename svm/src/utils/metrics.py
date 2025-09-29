# Fungsi untuk evaluasi model

import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from src.config import RESULTS_PATH, CLASSES

def evaluate_model(y_true, y_pred):
    """
    Menghitung dan mencetak metrik evaluasi.
    """
    # Akurasi
    accuracy = accuracy_score(y_true, y_pred)
    print(f"Akurasi Keseluruhan: {accuracy:.4f}\n")
    
    # Laporan Klasifikasi (Precision, Recall, F1-score)
    report = classification_report(y_true, y_pred, target_names=CLASSES)
    print("Laporan Klasifikasi:")
    print(report)
    
    # Simpan laporan ke file
    report_path = os.path.join(RESULTS_PATH, 'classification_report.txt')
    with open(report_path, 'w') as f:
        f.write(f"Akurasi Keseluruhan: {accuracy:.4f}\n\n")
        f.write("Laporan Klasifikasi:\n")
        f.write(report)
        
    return accuracy, report

def plot_confusion_matrix(y_true, y_pred):
    """
    Membuat dan menyimpan confusion matrix.
    """
    cm = confusion_matrix(y_true, y_pred)
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=CLASSES, yticklabels=CLASSES)
    plt.title('Confusion Matrix')
    plt.ylabel('Label Sebenarnya')
    plt.xlabel('Label Prediksi')
    
    # Simpan plot
    plot_path = os.path.join(RESULTS_PATH, 'confusion_matrix.png')
    plt.savefig(plot_path)
    print(f"Confusion matrix disimpan di: {plot_path}")
    plt.close()
