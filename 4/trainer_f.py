
from trainer import Ui_trainer
import os.path
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, pyqtSignal,QTimer
from imutils import paths
import face_recognition
import pickle
import cv2
import os


# grab the paths to the input images in our dataset
dataset='dataset/'
encoder='trainer/encodings.pickle'
imagePaths = list(paths.list_images(dataset))

total=0
knownEncodings = []
knownNames = []

class Mythread(QThread):
    #initializing signals
    change_value = pyqtSignal(int)
    driver_info = pyqtSignal(str)
    def run(self):
        global total
        # loop over the image paths
        for (i, imagePath) in enumerate(imagePaths):
            # extract the person name from the image path
            # GUI total status bar
            print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))
            total=len(imagePaths)


            # current name being trained
            name = imagePath.split(os.path.sep)[-2]

            # display current works
            self.change_value.emit(i)
            self.driver_info.emit(name)

            # load the input image and convert it from RGB (OpenCV ordering)
            # to dlib ordering (RGB)
            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # detect the (x, y)-coordinates of the bounding boxes
            # corresponding to each face in the input image
            boxes = face_recognition.face_locations(rgb, model='cnn')

            # compute the facial embedding for the face
            encodings = face_recognition.face_encodings(rgb, boxes)

            # loop over the encodings
            for encoding in encodings:
                # add each encoding + name to our set of known names and
                # encodings
                knownEncodings.append(encoding)
                knownNames.append(name)

        # dump the facial encodings + names to disk

        # GUI
        # writing to the new pickle
        self.driver_info.emit('serializing encodings...')

        data = {"encodings": knownEncodings, "names": knownNames}
        f = open(encoder, "wb")
        f.write(pickle.dumps(data))
        f.close()
        self.driver_info.emit('done')


class trainerwindow(QtWidgets.QMainWindow,Ui_trainer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.progressBar.setValue(0)

        self.timer_back2root = QTimer()



    def start(self):
        # display current works

        #start threading
        self.thread=Mythread()
        self.thread.change_value.connect(self.set_val)
        self.thread.driver_info.connect(self.set_driver)
        self.thread.start()




    def set_val(self,val):
        # set progress bar
        self.progressBar.setValue((val + 1) * (100 / total))
        self.pictures_info.setText('processing image:   ' + str(val + 1) +' / '+ str(total))

    def set_driver(self,name):
        self.drivers.setText(name)
        if name == 'done':
            # done training go back to root menu
            if not self.timer_back2root.isActive():
                # start timer
                self.timer_back2root.start(20)


#
# app = QApplication(sys.argv)
# trainer=trainerwindow()
# trainer.show()
# trainer.start()
#
#
# sys.exit(app.exec_())
