import cv2 as cv



if __name__ == '__main__':
    cameraCapture = cv.VideoCapture(0)
    fps = 30 #(int)(cameraCapture.get(cv.CAP_PROP_FPS))
    size = (int(cameraCapture.get(cv.CAP_PROP_FRAME_WIDTH)),
            int(cameraCapture.get(cv.CAP_PROP_FRAME_HEIGHT)))

    videoWriter = cv.VideoWriter('..\data\MyOutputVid-1.avi',cv.VideoWriter_fourcc('I','4','2','0'),fps,size)

    success ,frame = cameraCapture.read()
    numFrameRemaining = 10 * fps - 1
    while success and numFrameRemaining > 0:
        videoWriter.write(frame)
        success, frame = cameraCapture.read()
        numFrameRemaining -= 1

    cameraCapture.release()
