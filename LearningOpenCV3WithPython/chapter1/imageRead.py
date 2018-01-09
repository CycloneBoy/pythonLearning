import cv2 as cv
import numpy as np



if __name__ == '__main__':
    img1 = np.zeros((3, 3), dtype=np.uint8)
    print(img1)
    print(img1.shape)

    img2 = cv.cvtColor(img1, cv.COLOR_GRAY2BGR)

    img3 = cv.imread('..\data\\test1.png')
    cv.imwrite('test1.png',img3)

    grayImage = cv.imread('..\data\\test1.png',cv.IMREAD_GRAYSCALE)
    cv.imwrite('..\data\\test1Gray.png',grayImage)