import os.path
import cv2
import os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from fac_rec import Ui_fac_rec

#save.txt
save_path='save.txt'

#Intel Haarcascade file
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#for trainning xml file
recognizer = cv2.face.LBPHFaceRecognizer_create()

#path to dataset
dataset_path=('dataset/')

#path to yml
yml_path=('trainer/trainer.yml')

#font
font = cv2.FONT_HERSHEY_SIMPLEX


confirm_face=70
unlock_root=0
unlock_frame = 0
read_yml = 0
name_array = []


# import Opencv module



class fac_recwindow(QtWidgets.QMainWindow,Ui_fac_rec):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # create a timer
        self.timer = QTimer()

    # ================================Fac_Rec==================================
    def camera_init(self):
        global read_yml, name_array, unlock_root, confirm_face, unlock_frame
        self.cap = cv2.VideoCapture(0)




        # =============================================================================================================

        # how many frame would it take to unclock the car
        unlock_frame = 0
        # condition start dash cam if exist yml file
        read_yml = 0
        # Array to store the name
        name_array = []
        # unlock_root condition to go to root
        unlock_root = 0
        # open save.txt
        if os.path.isfile(save_path):
            with open(save_path, 'r+') as my_file:
                name_array = my_file.readlines()
        # if name_array is not empty
        if name_array:
            # Read trainer.yml
            if os.path.isfile(yml_path):
                # read the trainer.yml file
                recognizer.read(yml_path)
                read_yml = 1
            else:
                # GUI
                print('Error yml file')
        else:
            print('Error name_array is empty')
        # ==============================================================================================================

        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # if timer is stopped and read_yml is valid
        #if not self.timer.isActive() and read_yml == 1 and self.cap.isOpened():
        if not self.timer.isActive() and self.cap.isOpened():
            # start timer
            self.timer.start(10)



    def viewCam(self):
        global unlock_frame,read_yml
        if self.timer.isActive():
            # read image in BGR format
            ret, image = self.cap.read()
            # convert image to RGB format
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # ======================================================================================
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.2, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (225, 0, 0), 2)
                Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 60):
                    # increment unlock_frame
                    unlock_frame += 1
                    # get id to name according to name list

                    Id = name_array[Id - 1][:-1]
                    conf = "  {0}%".format(round(100 - conf))

                    # confirm face
                    if unlock_frame == confirm_face:
                        unlock_root = 1
                        # stop timer
                        self.timer.stop()
                        # release video capture
                        self.cap.release()
                        if not self.timer_main.isActive():
                            self.timer_main.start(20)
                else:
                    Id = "Unknown"
                    conf = "  {0}%".format(round(100 - conf))
                cv2.putText(image, str(Id), (x, y + h), font, 1, (0, 255, 0), 3)
                cv2.putText(image, str(conf), (x + 150, y + h - 5), font, 1, (0, 0, 255), 3)
            # ======================================================================================
            self.progressBar_for_camera.setValue(unlock_frame * (100 / confirm_face))
            # get image infos
            height, width, channel = image.shape
            step = channel * width
            # create QImage from image
            qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
            # show image in img_label
            self.camera.setScaledContents(True)
            self.camera.setPixmap(QPixmap.fromImage(qImg))
        else:
            pass





