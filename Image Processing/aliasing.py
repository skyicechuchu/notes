import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import ndimage
import os

# Path to your image file
image_path = 'Image Processing/assets/dota.png'
image = mpimg.imread(image_path)


# Convert the image to grayscale using the luminosity method
if image.ndim == 3:  # Check if the image is colored
    image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])  # Standard weights for RGB to grayscale

# Function to downsample the image to induce aliasing
def downsample(image, factor):
    print(len(image[::factor, ::factor]))
    return image[::factor, ::factor]

# Function to apply Gaussian filter for anti-aliasing
def antialias(image, sigma):
    return ndimage.gaussian_filter(image, sigma=sigma)

# Downsample the image (high factor can increase aliasing)
factor = 8
aliased_image = downsample(image, factor)

# Apply Gaussian filter before downsampling to reduce aliasing
smoothed_image = antialias(image, sigma=3)
anti_aliased_image = downsample(smoothed_image, factor)

# Plotting
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(image, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(aliased_image, cmap='gray')
axes[1].set_title('Aliased Image')
axes[1].axis('off')

axes[2].imshow(anti_aliased_image, cmap='gray')
axes[2].set_title('Anti-Aliased Image')
axes[2].axis('off')

plt.tight_layout()
plt.show()