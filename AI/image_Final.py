import numpy as np
import argparse
import imutils
import cv2

# translation
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image', required=True,
help = 'Path to the image')
args = vars(ap.parse_args())

image= cv2.imread(args['image'])
cv2.imshow('Original', image)
cv2.waitKey(0)

M = np.float32([[1,0,25], [0,1,50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('Shifted Down and Right', shifted)
cv2.waitKey(0)

M = np.float32([[1,0,-25], [0,1,-50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('Shifted Up and Left', shifted)
cv2.waitKey(0)

#rotate
ap  = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True, help='Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)

(h, w) = image.shape[:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow('Rotated by 25 Degrees', rotated)
cv2.waitKey(0)

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow('Rotated by -90 Degrees', rotated)
cv2.waitKey(0)

def rotate(image, angel, center = None, scale = 1.0):
    (h,w) = image.shape[:2]
    if center is None:
        center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angel, scale)
    rotate = cv2.warpAffine(image, M, (w,h))
    
    return rotated

import cv2
# import detect_face
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]
    # face_locations = detect_face(rgb_frame)
    # for top, right, bottom, left, gender_preds, max_age_preds, \
    #     idx_max_age_preds in face_locations:
    #     # Draw a box around the face
    #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.imshow('Video', frame)
    if cv2.waitKey(5) == 27 :
        break
video_capture.release()
cv2.destroyAllWindows()

import cv2
from imutils import translate
import numpy as np

image = cv2.imread("image.jpg")
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
#cv2.imshow("Original", image)

shifted = translate(image, 25, 50)
#cv2.imshow("Shift Down & Right", shifted)

shifted = translate(image, -25, -50)
#cv2.imshow("Shift Up & Left", shifted)

(h,w) = image.shape[:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
#cv2.imshow("Rotated by 45 degrees", rotated)

M = cv2.getRotationMatrix2D(center, -45, 0.5)
rotated = cv2.warpAffine(image, M, (w, h))
#cv2.imshow("Rotated by -45 degrees", rotated)
# 과제 : 회전시 이미지가 윈도우에 패킹(꼭 맞게)되도록 한다...
# 오늘 실습 예제의 기능들을 모두 imutils.py에 넣어 모듈화한다.
r = 150/ image.shape[1]
dim = (150, int(image.shape[0] *r))
resized = cv2.resize(image, dim, 
                     interpolation=cv2.INTER_AREA)
#cv2.imshow("Resized (Width)", resized)

print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 255: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

M = np.ones(image.shape, dtype="uint8")* 100
added = cv2.add(image, M)
cv2.imshow("Added", added)
M = np.ones(image.shape, dtype="uint8")* 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2

rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25,25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150,150), 150, 255, -1)
cv2.imshow("Circle", circle)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("And", bitwiseAnd)
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("Or", bitwiseOr)
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("Xor", bitwiseXor)

cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
mask = np.zeros(image.shape[:2], dtype="uint8")
print(mask.shape)
cv2.rectangle(mask, (25,25), (275, 275), 255, -1)
# cv2.imshow("Mask", mask)

bitwiseAnd = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("And", bitwiseAnd)

cv2.waitKey(0)
cv2.destroyAllWindows()