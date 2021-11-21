import os
import skimage
import skimage.io as io
from skimage import data, filters, exposure, feature
from skimage.filters import rank
from skimage.util.dtype import convert
from skimage import img_as_float, img_as_ubyte
from skimage.color import rgb2hsv, hsv2rgb, rgb2gray
from skimage.filters.edges import convolve
from matplotlib import pylab as plt  

def load(foldername):
    input = []
    for filename in os.listdir(foldername):
        input.append(img_as_float(io.imread(os.path.join(foldername, filename))))
    return input

def main():
    cars = load("./images")
    gray_cars = []
    for i in range(len(cars)):
        gray_cars.append(rgb2gray(cars[i]))
    print(gray_cars[0])

if __name__ == '__main__':
    main()