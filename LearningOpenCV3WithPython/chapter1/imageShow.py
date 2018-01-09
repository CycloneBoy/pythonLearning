import cv2 as cv
import numpy as np

if __name__ == '__main__':
    img = cv.imread('..\data\\test1.png')
    cv.imshow('my image',img)
    cv.waitKey()
    cv.destroyAllWindows()