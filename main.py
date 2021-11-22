import os
import numpy as np
import skimage
import skimage.io as io
from skimage import data, filters, exposure, feature
from skimage.filters import rank
from skimage.util.dtype import convert
from skimage import img_as_float, img_as_ubyte
from skimage.color import rgb2hsv, hsv2rgb, rgb2gray
from skimage.filters.edges import convolve
from matplotlib import pylab as plt
import cv2

def load(foldername):
    input = []
    for filename in os.listdir(foldername):
        input.append(cv2.imread((os.path.join(foldername, filename))))
    return input

def to_gray(list1 , list2):

    for item in list1:
        gray = cv2.cvtColor(item, cv2.COLOR_BGR2GRAY)  # convert to grey scale
        gray = cv2.bilateralFilter(gray, 13, 15, 15)
        edges = cv2.Canny(gray, 100,200)
        list2.append(edges)

def main():
    cars = load("./images")
    cars_image = []
    gray_cars = []
    for i in range(len(cars)):
        cars_image.append(cars[i])
    #print(cars_image[0])
    to_gray(cars_image,gray_cars)

    for car , car2 in zip(gray_cars, cars):

        imS = cv2.resize(car, (960, 540))
        cv2.imshow("output", imS)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        imS = cv2.resize(car2, (960, 540))
        cv2.imshow("output", imS)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()