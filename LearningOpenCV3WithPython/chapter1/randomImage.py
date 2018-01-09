import cv2 as cv
import numpy as np
import os

if __name__ == '__main__':
    randomByteArray = bytearray(os.urandom(120000))
    flatNumpyArray = np.array(randomByteArray)

    grayImage = flatNumpyArray.reshape(300,400)
    cv.imwrite('..\data\RandomGray.png',grayImage)

    bgrImage = flatNumpyArray.reshape(100,400,3)
    cv.imwrite('..\data\RandomColor.png',bgrImage)



    img = cv.imread('..\data\\test1.png')
    img[0,0] =[255,255,255]

    print(img.item(150,120,0))
    img.itemset((150,120,0),255)
    print(img.item(150,120,0))

    img[:,:,1] = 0
    cv.imwrite('..\data\\test1-1.png',img)

    my_roi = img[0:100,0:100]
    img[300:400,300:400] = my_roi
    cv.imwrite("..\data\\test1-2.png",img)

    print(img.shape)
    print(img.size)
    print(img.dtype)


