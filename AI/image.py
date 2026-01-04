from __future__ import print_function
import argparse
import cv2

image = cv2.imread('image.jpg')
print('width: {} pixels'.format(image.shape[1]))
print('height: {} pixels'.format(image.shape[0]))
print('channels: {} pixels'.format(image.shape[2]))
cv2.imshow('image before convert', image)
(b,g,r) = image[97,190]
print("Pixel at (97,190): Red : {}, Green : {}, Blue : {}".format(r,g,b))
image[97,190] = (0,255,0)
(b,g,r) = image[97,190]
print("Pixel at (97,190): Red : {}, Green : {}, Blue : {}".format(r,g,b))
cv2.imshow('image after convert', image)
cv2.waitKey(0)
cv2.destroyAllWindows()