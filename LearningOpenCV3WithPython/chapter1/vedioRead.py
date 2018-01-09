import cv2 as cv

if __name__ == '__main__':
    videoCapture = cv.VideoCapture('..\data\MyInutVid.avi')
    fps = (int)(videoCapture.get(cv.CAP_PROP_FPS))
    size = (int(videoCapture.get(cv.CAP_PROP_FRAME_WIDTH)),
            int(videoCapture.get(cv.CAP_PROP_FRAME_HEIGHT)))
    videoWriter = cv.VideoWriter('..\data\MyOutputVid.avi',cv.VideoWriter_fourcc('I','4','2','0'),fps,size)
    success,frame = videoCapture.read()
    while success:
        videoWriter.write(frame)
        success,frame = videoCapture.read()
