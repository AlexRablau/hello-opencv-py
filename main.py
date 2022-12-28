import numpy as np
import cv2 as cv

image = cv.imread('messi5.jpg')

for i in range(image.shape[0]):
  for j in range(image.shape[1]):
    if (i % 5 == 0):
      image[i, j] = [255, 0, 0]

cv.imwrite('messout.jpg', image)
