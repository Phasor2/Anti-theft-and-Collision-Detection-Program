import os.path
import os,sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from fac_rec import Ui_fac_rec
from PyQt5.QtWidgets import QApplication
import imutils
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import cv2



#Intel Haarcascade file
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#path to dataset
dataset_path=('dataset/')



#font
font = cv2.FONT_HERSHEY_SIMPLEX


confirm_face=10
unlock_root=0
unlock_frame = 0
read_yml = 0
name_array = []
dataset='dataset'
encoding='trainer/encodings.pickle'
data=0
# import Opencv module

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


class fac_recwindow(QtWidgets.QMainWindow,Ui_fac_rec):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # create a timer
        self.timer = QTimer()

    # ================================Fac_Rec==================================
    def camera_init(self):
        global read_yml, name_array, unlock_root, confirm_face, unlock_frame, data
        if os.path.isfile(encoding):
            self.cap = cv2.VideoCapture(0)

            data = pickle.loads(open(encoding, "rb").read())


            # how many frame would it take to unclock the car
            unlock_frame = 0


            # set timer timeout callback function
            self.timer.timeout.connect(self.viewCam)
            # if timer is stopped and read_yml is valid
            #if not self.timer.isActive() and read_yml == 1 and self.cap.isOpened():
            if not self.timer.isActive() and self.cap.isOpened():
                # start timer
                self.timer.start(10)
        else:
            pass



    def viewCam(self):
        global unlock_frame,read_yml,name_array
        if self.timer.isActive():
            # read image in BGR format
            #ret, image = self.cap.read()
            # convert image to RGB format
            #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # ======================================================================================
            # grab the frame from the threaded video stream and resize it
            # to 500px (to speedup processing)
            ret, frame = self.cap.read()
            #frame = imutils.resize(frame, width=500)

            # convert the input frame from (1) BGR to grayscale (for face
            # detection) and (2) from BGR to RGB (for face recognition)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # detect faces in the grayscale frame
            rects = detector.detectMultiScale(gray, scaleFactor=1.3,
                                              minNeighbors=5, minSize=(30, 30),
                                              flags=cv2.CASCADE_SCALE_IMAGE)

            #print(rects)
            #if rects["dt"]:
             #   print(rects[1])
            # OpenCV returns bounding box coordinates in (x, y, w, h) order
            # but we need them in (top, right, bottom, left) order, so we
            # need to do a bit of reordering
            boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

            #if boxes[0] < 93 or boxes[1] < 488 or boxes[2] < 360 or boxes[3] < 211:
            #boxes = []
            # compute the facial embeddings for each face bounding box
            encodings = face_recognition.face_encodings(frame, boxes)
            names = []

            # loop over the facial embeddings
            for encoding in encodings:
                # attempt to match each face in the input image to our known
                # encodings
                matches = face_recognition.compare_faces(data["encodings"],
                                                         encoding)
                name = "Unknown"

                # check to see if we have found a match
                if True in matches:
                    # find the indexes of all matched faces then initialize a
                    # dictionary to count the total number of times each face
                    # was matched
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}

                    # loop over the matched indexes and maintain a count for
                    # each recognized face face
                    for i in matchedIdxs:
                        name = data["names"][i]
                        counts[name] = counts.get(name, 0) + 1

                    # determine the recognized face with the largest number
                    # of votes (note: in the event of an unlikely tie Python
                    # will select first entry in the dictionary)
                    name = max(counts, key=counts.get)

                # update the list of names
                names.append(name)

            # loop over the recognized faces
            for ((top, right, bottom, left), name) in zip(boxes, names):

                #threshold for how far to detect
                #if right > 430 and bottom >400 :
                if right > 400 and bottom >390 :
                    #print(right,bottom)
                    # draw the predicted face name on the image
                    cv2.rectangle(frame, (left, top), (right, bottom),
                                  (0, 255, 0), 2)
                    y = top - 15 if top - 15 > 15 else top + 15
                    cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                                0.75, (0, 255, 0), 2)
                    if name!="Unknown":
                        unlock_frame += 1

            # update the FPS counter
            #fps.update()
            # ======================================================================================

            if unlock_frame == confirm_face:
                # stop timer
                self.timer.stop()
                # release video capture
                self.cap.release()
                if not self.timer_main.isActive():
                    self.timer_main.start(20)

            self.progressBar_for_camera.setValue(unlock_frame * (100 / confirm_face))


            # get image infos
            height, width, channel = frame.shape
            step = channel * width
            # create QImage from image
            qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)

            # show image in img_label
            self.camera.setScaledContents(True)
            self.camera.setPixmap(QPixmap.fromImage(qImg))
        else:
            pass



#
# app = QApplication(sys.argv)
# fac_rec=fac_recwindow()
# fac_rec.show()
# fac_rec.camera_init()
#
# sys.exit(app.exec_())
