import os.path
import cv2
import os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
import sys
from cap_new_user import Ui_cap_new_user
from PIL import Image
import numpy as np

#save.txt
save_path='save.txt'

#Intel Haarcascade file
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#path to dataset
dataset_path=('dataset/')

# Initialize amount of number to take for training
sample_number = 5
counter=0



class cap_new_userwindow(QtWidgets.QMainWindow,Ui_cap_new_user):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # create a timer

        #this timer will go to start video loop
        self.timer = QTimer()

        #this timer will start to take picture
        self.timer2 = QTimer()

        #this timer to get to next window
        self.timer3 = QTimer()
        self.new_name = ''

        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        self.timer2.timeout.connect(self.take_sample)

        #button for start capture
        self.start.clicked.connect(self.take_sample)




    def take_sample(self):
        global counter,sample_number
        # increment counter
        counter += 1

        # dirrectory name_that contain sample
        dir_name_sample = dataset_path + self.new_name
        # make name directory
        if not os.path.isdir(dir_name_sample) and counter == 1:
            os.makedirs(dir_name_sample)

        # getting image for saving
        p = self.qImg

        #set progress bar
        self.progressBar.setValue(counter * (100 / sample_number))

        #save images
        p.save(dir_name_sample +'/'+str(counter)+'.jpg', 'jpg')
        #start recursion timer
        if not self.timer2.isActive():
            self.timer2.start(2000)

        #done taking sample clean up and call trainer xml
        if counter == sample_number and self.timer2.isActive():
            self.timer.stop()
            self.timer2.stop()
            # release video capture
            self.cap.release()

            # done trainer go to training window
            if not self.timer3.isActive():
                # start timer
                self.timer3.start(20)



    # ================================Fac_Rec==================================
    def camera_init(self):
        global counter
        self.cap = cv2.VideoCapture(0)
        self.progressBar.setValue(0)
        counter =0

        # if timer is not active and camera is active start timer
        if not self.timer.isActive() and self.cap.isOpened():
            # start timer
            self.timer.start(20)



    def viewCam(self):
        if self.timer.isActive():
            # read image in BGR format
            ret, image = self.cap.read()

            # convert image to RGB format

            #t_image for storing and training
            t_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            #s_image for showing for the user the tracking
            s_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # gray is for haarcase face detection
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # ======================================================================================
            # start to detect faces
            faces = detector.detectMultiScale(gray, 1.3, 5)


            # start drawing a rectangle for faces
            for (x, y, w, h) in faces:
                cv2.rectangle(s_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # ====================================================================================

            # get image infos
            height, width, channel = image.shape
            step = channel * width
            # create QImage from image
            self.qImg = QImage(t_image.data, width, height, step, QImage.Format_RGB888)

            # getting q image for saving
            self.s_Img = QImage(s_image.data, width, height, step, QImage.Format_RGB888)

            # show image in img_label
            self.camera.setScaledContents(True)
            self.camera.setPixmap(QPixmap.fromImage(self.s_Img))

        else:
            pass
#
# app = QApplication(sys.argv)
# cap_new_user=cap_new_userwindow()
# cap_new_user.show()
# cap_new_user.camera_init()
#
# sys.exit(app.exec_())
#
#
#























