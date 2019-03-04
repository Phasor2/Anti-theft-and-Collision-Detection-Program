from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QProgressBar, QPushButton, QVBoxLayout
import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time
from PyQt5 import QtWidgets
from trainer import Ui_trainer
import os.path
import cv2
import os,sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from imutils import paths
import face_recognition
import pickle
import cv2
import os

from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QTimer


# grab the paths to the input images in our dataset
dataset='dataset/'
encoder='trainer/encodings.pickle'
imagePaths = list(paths.list_images(dataset))


total=0
knownEncodings = []
knownNames = []







# pyqtsignal with this we can send data between worker and our thread


class MyThread(QThread):
    # Create a counter thread

    change_value = pyqtSignal(int)

    def run(self):
        global total
        # loop over the image paths
        for (i, imagePath) in enumerate(imagePaths):
            # extract the person name from the image path
            # GUI total status bar
            print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))
            total = len(imagePaths)

            # current name being trained
            name = imagePath.split(os.path.sep)[-2]

            # display current works
            self.change_value.emit(i)
            # self.pictures_info.setText('processing image' + str(i + 1) + str(len(imagePaths)))
            # self.drivers.setText(name)

            # set progress bar
            # self.progressBar.setValue(i + 1 * (100 / len(imagePaths)))

            # load the input image and convert it from RGB (OpenCV ordering)
            # to dlib ordering (RGB)
            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # detect the (x, y)-coordinates of the bounding boxes
            # corresponding to each face in the input image
            boxes = face_recognition.face_locations(rgb, model='hog')

            # compute the facial embedding for the face
            encodings = face_recognition.face_encodings(rgb, boxes)

            # loop over the encodings
            for encoding in encodings:
                # add each encoding + name to our set of known names and
                # encodings
                knownEncodings.append(encoding)
                knownNames.append(name)

        # dump the facial encodings + names to disk
        #self.drivers.setText('DONE')
        #self.pictures_info.setText('serializing encodings...')
        # GUI
        # writing to the new pickle
        data = {"encodings": knownEncodings, "names": knownNames}
        f = open(encoder, "wb")
        f.write(pickle.dumps(data))
        f.close()



class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 ProgressBar"
        self.top = 200
        self.left = 500
        self.width = 300
        self.height = 100
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        self.progressbar = QProgressBar()
        # self.progressbar.setOrientation(Qt.Vertical)
        self.progressbar.setMaximum(100)

        self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey;border-radius:8px;padding:1px}"
                                       "QProgressBar::chunk {background:yellow}")

        # qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 red, stop: 1 white);

        # self.progressbar.setStyleSheet("QProgressBar::chunk {background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 red, stop: 1 white); }")
        # self.progressbar.setTextVisible(False)
        vbox.addWidget(self.progressbar)

        self.button = QPushButton("Start Progressbar")
        self.button.clicked.connect(self.startProgressBar)
        self.button.setStyleSheet('background-color:yellow')
        vbox.addWidget(self.button)

        self.setLayout(vbox)

        self.show()

    def startProgressBar(self):
        self.thread = MyThread()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()

    def setProgressVal(self, val):
        global total
        print(val)
        self.progressbar.setValue(val + 1 * (100 / total))


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

