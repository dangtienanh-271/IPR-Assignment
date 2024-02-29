import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

# Load the image
img_path = 'a.png'
assert os.path.exists(img_path), "File could not be read, check with os.path.exists()"
img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

# Check if image is loaded successfully
assert img is not None, "Unable to load the image."

# Apply median blur
img = cv.medianBlur(img, 5)

# Apply global thresholding
ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# Apply adaptive mean thresholding
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

# Apply adaptive Gaussian thresholding
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

# Plot the images
titles = ['Original Image', 'Global Thresholding (v = 127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()