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

#for trainning xml file
recognizer = cv2.face.LBPHFaceRecognizer_create()

#path to dataset
dataset_path=('dataset/')


#path to yml
yml_path=('trainer/trainer.yml')

#font
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize amount of number to take for training
sample_number = 30
counter=0
first=0
complete = 0


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
        self.Id=0

        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        self.timer2.timeout.connect(self.take_sample)

        #button for start capture
        self.start.clicked.connect(self.take_pic)

    # Trainer produce trainer.yml for exam_face
    def trainer(self):
        global first, counter
        def trainer_xml(path):
            # get the path of all the files in the folder
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
            # create empth face list
            faceSamples = []
            # create empty ID list
            Ids = []
            # now looping through all the image paths and loading the Ids and the images
            for imagePath in imagePaths:

                # Updates in Code
                # ignore if the file does not have jpg extension :
                if (os.path.split(imagePath)[-1].split(".")[-1] != 'jpg'):
                    continue

                # loading the image and converting it to gray scale
                pilImage = Image.open(imagePath).convert('L')
                # Now we are converting the PIL image into numpy array
                imageNp = np.array(pilImage, 'uint8')
                # getting the Id from the image
                Id = int(os.path.split(imagePath)[-1].split(".")[1])
                # extract the face from the training image sample
                faces = detector.detectMultiScale(imageNp)
                # If a face is there then append that in the list as well as Id of it
                for (x, y, w, h) in faces:
                    faceSamples.append(imageNp[y:y + h, x:x + w])
                    Ids.append(Id)
            return faceSamples, Ids

        faces, Ids = trainer_xml(dataset_path)
        recognizer.train(faces, np.array(Ids))
        recognizer.save(yml_path)

        #reset values for next time
        first=0
        counter=0
        #done trainer go back to manage_driver_menu
        if not self.timer3.isActive():
            # start timer
            self.timer3.start(20)

    def take_pic(self):
        global first
        if not first:
            first=1
            p = self.qImg
            p.save('preview/'+str(self.Id), 'png')
        if not self.timer2.isActive():
            self.timer2.start(1000)


    # ================================Fac_Rec==================================
    def camera_init(self):
        global sample_number, complete,first
        self.cap = cv2.VideoCapture(0)

        first = 0


        self.roi_gray = 0
        self.progressBar.setValue(0)

        # if timer is stopped and read_yml is valid
        if not self.timer.isActive() and self.cap.isOpened():
            # start timer
            self.timer.start(20)

    def take_sample(self):
        global counter,sample_number
        Id=self.Id

        if counter != sample_number:
            counter += 1
            self.progressBar.setValue(counter * (100 / sample_number))
        # storing the driver face in the dataset folder as jpg
            cv2.imwrite("dataset/User." + str(Id) + "." + str(counter) + ".jpg",self.roi_gray)


        #done taking sample clean up and call trainer xml
        else:
            self.timer.stop()
            self.timer2.stop()
            # release video capture
            self.cap.release()
            self.trainer()


    def viewCam(self):
        global sample_number, first,counter
        Id=1
        if self.timer.isActive():
            # read image in BGR format
            ret, image = self.cap.read()

            # convert image to RGB format
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            if first:
                first=1
            #if first:
            # ======================================================================================
                # turn image into gray
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # start to detect faces
                faces = detector.detectMultiScale(gray, 1.3, 5)


                 # start drawing a rectangle for faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    self.roi_gray = gray[y:y + h, x:x + w]

                # ====================================================================================

                    # get image infos
            height, width, channel = image.shape
            step = channel * width
            # create QImage from image
            self.qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
            # show image in img_label
            self.camera.setScaledContents(True)
            self.camera.setPixmap(QPixmap.fromImage(self.qImg))

        else:
            pass

#app = QApplication(sys.argv)
#cap_new_user=cap_new_userwindow()
#cap_new_user.show()
#cap_new_user.camera_init()

#sys.exit(app.exec_())


























