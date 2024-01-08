from PIL import Image
import os

dataset_path = "landscape_images\color"

# Expected image size
expected_size = (150, 150)

# Function to detect images with different sizes
def detect_images_with_different_sizes(dataset_path, expected_size):
    inconsistent_sizes = []

    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            image_path = os.path.join(root, file)

            # Open the image using PIL
            with Image.open(image_path) as img:
                # Check if the image size is different from the expected size
                if img.size != expected_size:
                    inconsistent_sizes.append((image_path, img.size))

    return inconsistent_sizes

# Detect images with different sizes
inconsistent_images = detect_images_with_different_sizes(dataset_path, expected_size)

# Print or handle the inconsistent images
if inconsistent_images:
    print("Images with different sizes:")
    for image_path, size in inconsistent_images:
        print(f"Image: {image_path}, Size: {size}")
else:
    print("No images with different sizes found.")