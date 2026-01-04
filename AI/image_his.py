import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg')
cv2.imshow("Original", image)
chans = cv2.split(image)
colors = ('b','g','r')

for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist(chan, [0], None, [256], [0,256])
    plt.plot(hist)
    plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

