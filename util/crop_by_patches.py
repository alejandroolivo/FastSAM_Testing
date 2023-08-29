import os
from PIL import Image

# Define source and destination directories
src_dir = r"./images/tomates/"
dst_dir = r"./images/tomates/Cropped/"

# Create destination directory if it doesn't exist
os.makedirs(dst_dir, exist_ok=True)

def generate_patches(img, num_patches):
    """Divide an image into num_patches x num_patches patches."""
    width, height = img.size
    patch_width = width // num_patches
    patch_height = height // num_patches
    patches = []

    for i in range(num_patches):
        for j in range(num_patches):
            left = i*patch_width
            upper = j*patch_height
            right = (i+1)*patch_width
            lower = (j+1)*patch_height
            patch = img.crop((left, upper, right, lower))
            patches.append(patch)
    
    return patches

# For every image file
for filename in os.listdir(src_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):  # add or modify image file extensions as needed
        image = Image.open(os.path.join(src_dir, filename))
        
        # Generate patches
        patches = generate_patches(image, 2)  # 4x4 patches

        # Save each patch to the destination directory
        for i, patch in enumerate(patches):
            patch_filename = os.path.splitext(filename)[0] + f"_patch{i}" + os.path.splitext(filename)[1]
            patch.save(os.path.join(dst_dir, patch_filename))
