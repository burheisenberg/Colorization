import os
from PIL import Image

folder_path = "landscape_images\color"  # Replace with your actual folder path

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust for other extensions if needed
        image_path = os.path.join(folder_path, filename)
        try:
            with Image.open(image_path) as img:
                channels = len(img.getbands())
                if channels!=3:
                    print(f"{filename}: {channels} channels")
        except OSError:
            print(f"Error opening {filename}")