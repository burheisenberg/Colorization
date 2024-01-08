import os
from PIL import Image

input_path = "landscape_images\color"  # Replace with your actual folder path
output_path = "landscape_images\gray"

for filename in os.listdir(input_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust for other extensions if needed
        image_path = os.path.join(input_path, filename)
        try:
            with Image.open(image_path) as img:
                channels = len(img.getbands())
                if channels == 3:  # Check for 3 channels
                    gray_img = img.convert("L")  # Convert to grayscale
                    output_image_path = os.path.join(output_path, "" + filename)  # Construct output path
                    gray_img.save(output_image_path)  # Save grayscale image
                    print(f"{filename} converted to grayscale and saved as {output_path}")
                else:
                    print(f"{filename} already has {channels} channels")
        except OSError:
            print(f"Error opening {filename}")