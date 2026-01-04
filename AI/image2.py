from __future__ import print_function
import argparse
import cv2
# 이미지 색 바꾸기
image = cv2.imread('image.jpg')
print('width: {} pixels'.format(image.shape[1]))
print('height: {} pixels'.format(image.shape[0]))
cv2.imshow('image before convert', image)
corner = image[0:100, 0:100]
cv2.imshow('cutted image', corner)
corner = (0,0,0)
image[0:100, 0:100] = corner

image[97,190] = (0,255,0)
(b,g,r) = image[97,190]
print("Pixel at (97,190): Red : {}, Green : {}, Blue : {}".format(r,g,b))
cv2.imshow('image after convert', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 사각형그리기
import numpy as np
import cv2
canvas = np.zeros((300,300,3), dtype='uint8')
green = (0,255,0)
cv2.line(canvas, (0,0), (300, 300), green)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

red = (0,0,255)
cv2.line(canvas, (300, 0), (0,300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (10,10), (60,60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 255), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey()

blue= (255, 0, 0)
cv2.rectangle(canvas, (200, 50),(225,125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 원그리기
canvas = np.zeros((300,300,3), dtype='uint8')
(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)
white = (255,255,255)

for r in range(0, 175, 25):
    cv2.circle(canvas,(centerX, centerY), r, white)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

for i in range(0,25):
    radius = np.random.randint(5,high = 200)
    color = np.random.randint(0, high=256, size = (3,)).tolist()
    pt = np.random.randint(0, high = 300, size =(2,))
    cv2.circle(canvas, tuple(pt), radius, color, -1)
cv2.imshow("Canva", canvas)
cv2.waitKey(0)