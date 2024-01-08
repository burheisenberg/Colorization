import os
from PIL import Image, ImageCms
from torch.utils.data import Dataset
from torchvision import transforms

class CustomDataset(Dataset):
    def __init__(self, input_folder, output_folder, transform=None):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.transform = transform

        self.input_images = os.listdir(input_folder)
        self.output_images = os.listdir(output_folder)

    def __len__(self):
        return min(len(self.input_images), len(self.output_images))

    def __getitem__(self, idx):
        input_path = os.path.join(self.input_folder, self.input_images[idx])
        output_path = os.path.join(self.output_folder, self.output_images[idx])

        input_image = Image.open(input_path) #.convert('L')
        output_image = Image.open(output_path) #.convert('RGB')  # Convert to grayscale if necessary

        if self.transform:
            input_image = self.transform(input_image)
            output_image = self.transform(output_image)

        return input_image, output_image

# Example usage
if __name__ == "__main__":
    input_folder = "landscape_images\gray"
    output_folder = "landscape_images\color"
    transform = transforms.Compose([
        transforms.ToTensor(),
    ])

    dataset = CustomDataset(input_folder, output_folder, transform=transform)

    # Example of iterating through the dataset
    for i in range(len(dataset)):
        input_image, output_image = dataset[i]
        if input_image.shape[1] != 150 or input_image.shape[2] != 150:
            print(f"For {i}, Input image shape: {input_image.shape}, Output image shape: {output_image.shape}")