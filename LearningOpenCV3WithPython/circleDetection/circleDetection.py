import cv2
import numpy as np

if __name__ == '__main__':
    # 载入并显示图片
    img = cv2.imread('circle.jpg')
    cv2.imshow('my image',img)

    # 降噪（模糊处理用来减少瑕疵点）
    result = cv2.blur(img, (5, 5))
    # cv2.imshow('blur 2', result)

    # 灰度化,就是去色（类似老式照片）
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('cvtColor 3', gray)

    # param1的具体实现，用于边缘检测
    canny = cv2.Canny(img, 40, 80)
    # cv2.imshow('canny 4', canny)

    # 霍夫变换圆检测
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 50, param1=80,
                               param2=30, minRadius=110, maxRadius=150)



    print(str(circles))

    print('-------------我是条分割线-----------------')
    # 根据检测到圆的信息，画出每一个圆
    for circle in circles[0]:
        # 圆的基本信息
        print(circle[2])
        # 坐标行列(就是圆心)
        x = int(circle[0])
        y = int(circle[1])
        # 半径
        r = int(circle[2])
        # 在原图用指定颜色圈出圆，参数设定为int所以圈画存在误差
        img = cv2.circle(img, (x, y), r, (0, 255, 255),3,8,0)

        ox = int(x + r/2.0)
        oy = int(y + r/2.0)
        img = cv2.circle(img, (x, y), 2, (0, 0, 255),2,8,0)

    # 显示新图像
    cv2.imshow('find circle', img)
    cv2.imwrite('find.jpg', img)

    cv2.waitKey()
    cv2.destroyAllWindows()