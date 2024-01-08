from PIL import Image
import os

dataset_path = "landscape_images/color"
output_path = "landscape_images/color"  # Specify the output path for resized images

# Expected image size
expected_size = (150, 150)

# Function to detect and resize images with different sizes
def resize_images(dataset_path, output_path, expected_size):
    os.makedirs(output_path, exist_ok=True)
    
    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            image_path = os.path.join(root, file)

            # Open the image using PIL
            with Image.open(image_path) as img:
                # Check if the image size is different from the expected size
                if img.size != expected_size:
                    # Resize the image to the expected size
                    resized_img = img.resize(expected_size, Image.Resampling.LANCZOS)

                    # Save the resized image to the output path
                    output_image_path = os.path.join(output_path, file)
                    resized_img.save(output_image_path)

# Resize images with different sizes
resize_images(dataset_path, output_path, expected_size)