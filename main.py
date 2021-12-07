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
import imutils

def load(foldername):
    input = []
    count = 0
    for filename in os.listdir(foldername):
        print(str(count) + ": " + str(filename))
        count += 1
        input.append(cv2.imread((os.path.join(foldername, filename))))
    return input
def to_gray(list1 , list2):
    count = 0
    for item in list1:
        gray = cv2.cvtColor(item, cv2.COLOR_BGR2GRAY)  # convert to grey scale
        gray = cv2.Canny(gray, 150,200)
        contours, trash = cv2.findContours(gray,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key = cv2.contourArea, reverse = True)[:30]
        screenCnt = None
        found = False
        for c in contours:
            approx = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c,True), True)
            #print(approx)
            if len(approx) == 4:
                screenCnt = approx
                #print("--------------")
                found = True
                break
        blurred = item.copy()
        print(count)
        count += 1
        if found:
            new_image = cv2.drawContours(item,[screenCnt],0,[255,0,0],-1)
        else:
            new_image = item
        blurred = cv2.blur(blurred, (50,50))
        #mask = np.zeros(image.shape, dtype=np.uint8)
        # for i in range(len(new_image)):
        #     for j in range(len(new_image[i])):
        #         if(new_image[i][j][0] == 255):
        #             new_image[i][j] = blurred[i][j]
        #list2.append(blurred)
        list2.append(new_image)


def main():
    cars = load("./images")
    cars_image = []
    gray_cars = []
    for i in range(len(cars)):
        cars_image.append(cars[i])
    #print(cars_image[0])
    to_gray(cars_image,gray_cars)    

    for car in gray_cars:

        imS = cv2.resize(car, (960, 540))
        cv2.imshow("output", imS)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()