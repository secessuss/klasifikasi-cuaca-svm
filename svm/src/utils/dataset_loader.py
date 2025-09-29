# Fungsi untuk memuat gambar

import os
import cv2
import numpy as np
from tqdm import tqdm
from src.config import CLASSES

def augment_image(image):
    """
    Menerapkan augmentasi sederhana pada sebuah gambar.
    """
    augmented_images = [image] # Mulai dengan gambar asli

    # 1. Flip Horizontal
    flipped_h = cv2.flip(image, 1)
    augmented_images.append(flipped_h)

    # 2. Perubahan Kecerahan (sedikit lebih terang dan lebih gelap)
    # Gunakan np.clip untuk memastikan nilai piksel tetap dalam rentang 0-255
    brighter = np.clip(image * 1.2, 0, 255).astype(np.uint8)
    darker = np.clip(image * 0.8, 0, 255).astype(np.uint8)
    augmented_images.append(brighter)
    # augmented_images.append(darker) # Bisa ditambahkan jika perlu lebih banyak data

    return augmented_images


def load_images_from_folder(folder_path, use_augmentation=True):
    """
    Memuat semua gambar dan labelnya dari subdirektori kelas.

    Args:
        folder_path (str): Path ke direktori utama dataset.
        use_augmentation (bool): Terapkan augmentasi jika True.

    Returns:
        tuple: Tuple berisi (list_gambar, list_label).
    """
    images = []
    labels = []
    
    print(f"Memuat gambar dari {folder_path}...")
    
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"Direktori dataset tidak ditemukan di: {folder_path}")

    for class_label, class_name in enumerate(CLASSES):
        class_path = os.path.join(folder_path, class_name)
        if not os.path.isdir(class_path):
            print(f"Peringatan: Direktori untuk kelas '{class_name}' tidak ditemukan di {class_path}")
            continue
            
        for filename in tqdm(os.listdir(class_path), desc=f"Loading {class_name}"):
            img_path = os.path.join(class_path, filename)
            try:
                img = cv2.imread(img_path)
                if img is not None:
                    # Menerapkan augmentasi
                    if use_augmentation:
                        augmented = augment_image(img)
                        for aug_img in augmented:
                            images.append(aug_img)
                            labels.append(class_label)
                    else:
                        images.append(img)
                        labels.append(class_label)
                else:
                    print(f"Peringatan: Gagal membaca gambar {img_path}")
            except Exception as e:
                print(f"Error saat memproses gambar {img_path}: {e}")
                
    print(f"Total gambar yang berhasil dimuat (setelah augmentasi): {len(images)}")
    return images, labels
