import numpy as np
import pytest
from src.preprocessing.image_preprocessing import (
    resize_image,
    to_grayscale,
    normalize_image,
    preprocess_image_for_feature_extraction
)
from src.config import IMAGE_SIZE

@pytest.fixture
def sample_image():
    """Membuat gambar sampel 3-channel (BGR) untuk testing."""
    # Gambar 200x150 dengan 3 channel, nilai piksel dari 0-255
    return np.random.randint(0, 256, (150, 200, 3), dtype=np.uint8)

def test_resize_image(sample_image):
    """Test apakah fungsi resize menghasilkan ukuran yang benar."""
    resized = resize_image(sample_image)
    # IMAGE_SIZE adalah (width, height), shape adalah (height, width, channels)
    assert resized.shape == (IMAGE_SIZE[1], IMAGE_SIZE[0], 3)

def test_to_grayscale(sample_image):
    """Test apakah konversi ke grayscale menghilangkan channel warna."""
    gray = to_grayscale(sample_image)
    assert len(gray.shape) == 2 # Harus hanya 2 dimensi (height, width)
    assert gray.shape == (150, 200)

def test_normalize_image(sample_image):
    """Test apakah normalisasi menghasilkan nilai piksel antara 0 dan 1."""
    float_image = sample_image.astype(np.float32)
    normalized = normalize_image(float_image)
    assert normalized.min() >= 0.0
    assert normalized.max() <= 1.0
    assert normalized.dtype == np.float32

def test_preprocess_image_for_feature_extraction(sample_image):
    """Test pipeline preprocessing secara keseluruhan."""
    normalized_gray, normalized_color = preprocess_image_for_feature_extraction(sample_image)
    
    # Cek output grayscale
    assert len(normalized_gray.shape) == 2
    assert normalized_gray.shape == (IMAGE_SIZE[1], IMAGE_SIZE[0])
    assert normalized_gray.min() >= 0.0
    assert normalized_gray.max() <= 1.0
    
    # Cek output color
    assert normalized_color.shape == (IMAGE_SIZE[1], IMAGE_SIZE[0], 3)
    assert normalized_color.min() >= 0.0
    assert normalized_color.max() <= 1.0
