#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 10:48
# @Author  : CycloneBoy
# @Site    : 
# @File    : cameo.py
# @Software: PyCharm

import cv2

from LearningOpenCV3WithPython.chapter2 import filters
from LearningOpenCV3WithPython.chapter2.managers import WindowManager,CaptureManager


class Cameo(object):

    def __init__(self):
        self._windowManager = WindowManager('Cameo',self.onKeypress)

        self._captureManager = CaptureManager(
                cv2.VideoCapture(0),self._windowManager,True)

        self._curveFilter = filters.BGRPortraCurveFilter()


    def run(self):
        """Run the main loop"""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            # TODO: Filter the frame
            filters.strokeEdges(frame,frame)
            self._curveFilter.apply(frame,frame)

            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self,keycode):
        """Handle a keypress

        space   -> Take a screenshsot
        tab     -> Start/Stop recording a screenshot.png
        escape  ->  Quit.

        """

        if keycode == 32:#space
            print("screenshot")
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9:  #tab
            if not self._captureManager.isWritingVideo:
                print("start record vedio")
                self._captureManager.startWritingVideo('screencast.avi')
            else:
                print("stop record vedio")
                self._captureManager.stopWritingVideo()
        elif keycode == 27: # escape
            self._windowManager.destroyWindow()

if __name__ == '__main__':
    Cameo().run()

