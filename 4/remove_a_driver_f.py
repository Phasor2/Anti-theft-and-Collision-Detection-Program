import os.path
import cv2
import os
import shutil
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
import sys
from remove_a_driver import Ui_remove_a_driver
from PIL import Image
import numpy as np

#path to dataset
dataset_path=('dataset/')

#preview image
preview_path=('preview/')


#path to yml
yml_path=('trainer/trainer.yml')

#font
font = cv2.FONT_HERSHEY_SIMPLEX



#path to dataset
dataset=('dataset/')

name_array=[]
total=0
current=0
class remove_a_driverwindow(QtWidgets.QMainWindow,Ui_remove_a_driver):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.left.clicked.connect(self.go_left)
        self.right.clicked.connect(self.go_right)
        self.remove.clicked.connect(self.delete)



    def delete(self):
        global current, name_array, total

        if not name_array:
            pass
        else:
            shutil.rmtree( 'dataset/'+ name_array[current-1], ignore_errors=False, onerror=None)


            # Pop deleted name in name_array
            name_array.pop(current - 1)


            #update trainer
            if name_array:
                # calling the trainer fuction
                # self.trainer()
                pass
            #just remove trainer
            else:
               if os.path.isfile(os.path.join('trainer/','encodings.pickle')):
                    os.remove(os.path.join('trainer/','encodings.pickle'))


        # load the remove function again
        self.remove_f()

    def update_info(self):
        global current, name_array, total

        pixmap = QPixmap('dataset/'+ name_array[current-1] +'/1.jpg')
        if name_array:
            self.id_label.setText(name_array[current-1]+' ' + 'person : ' + str(current)+ ' out of '+ str(total))
        else:
            self.id_label.setText(' ')
        #load image preview
        self.preview_image.setScaledContents(True)
        self.preview_image.setPixmap(pixmap)



    def go_left(self):
        global current, name_array
        if not name_array:
            self.preview_image.setText('No driver to remove !')
            self.id_label.setText(' ')
        else:
            if current==1:
                current=len(name_array)
            else:
                current=current-1
            self.update_info()

    def go_right(self):
        global  current,name_array
        if not name_array:
            self.preview_image.setText('No driver to remove !')
            self.id_label.setText(' ')
        else:
            if current==len(name_array):
                current=1
            else:
                current=current+1
            self.update_info()

    #start here
    def remove_f(self):
        global name_array,total,current
        # open save.txt
        # list names in dataset directory
        name_array = os.listdir(dataset)

        if not name_array:
            self.preview_image.setText('No driver to remove !')
            self.id_label.setText(' ')
        #start with Id = 1
        else:
            total=len(name_array)
            current=1
            self.update_info()

        # Trainer produce trainer.yml for exam_face

    # def trainer(self):
    #     global first, counter
    #
    #     def trainer_xml(path):
    #         # get the path of all the files in the folder
    #         imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    #         # create empth face list
    #         faceSamples = []
    #         # create empty ID list
    #         Ids = []
    #         # now looping through all the image paths and loading the Ids and the images
    #         for imagePath in imagePaths:
    #
    #             # Updates in Code
    #             # ignore if the file does not have jpg extension :
    #             if (os.path.split(imagePath)[-1].split(".")[-1] != 'jpg'):
    #                 continue
    #
    #             # loading the image and converting it to gray scale
    #             pilImage = Image.open(imagePath).convert('L')
    #             # Now we are converting the PIL image into numpy array
    #             imageNp = np.array(pilImage, 'uint8')
    #             # getting the Id from the image
    #             Id = int(os.path.split(imagePath)[-1].split(".")[1])
    #             # extract the face from the training image sample
    #             faces = detector.detectMultiScale(imageNp)
    #             # If a face is there then append that in the list as well as Id of it
    #             for (x, y, w, h) in faces:
    #                 faceSamples.append(imageNp[y:y + h, x:x + w])
    #                 Ids.append(Id)
    #         return faceSamples, Ids
    #
    #     faces, Ids = trainer_xml(dataset_path)
    #     recognizer.train(faces, np.array(Ids))
    #     recognizer.save(yml_path)
#
# app = QApplication(sys.argv)
# remove_a_driver=remove_a_driverwindow()
# remove_a_driver.show()
# remove_a_driver.remove_f()
# sys.exit(app.exec_())
#
