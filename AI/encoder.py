import tensorflow as tf
from keras.utils import np_utils
import matplotlib.pyplot as plt
import numpy as np
from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.resahpe((len(x_test), np.prod(x_test.shape[1:])))
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

def plot_image(data, classes, width=28, height=28, row_len=3):
    for i in range(10):
        idxs = (classes == i)
        autoencoders = data[idxs][0:10]
        
    for j in range(row_len):
        plt.subplot(row_len, 10, i + j*10 + 1)
        plt.imshow(autoencoders[j].reshape(width, height), cmap = 'gray')
        if j == 0:
            plt.title(1)
        plt.axis('off')
    plt.show()
classes = np.argmax(y_train, 1)
plot_image(x_train, classes)