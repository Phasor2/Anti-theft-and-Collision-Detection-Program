# Phong Nguyen
# ECE 412, Winter 2019
# Capstone Project: Anti-theft and Collision detection
# 4/3/2019

import sys
from PyQt5.QtWidgets import QApplication
from mainmenu_f import mainmenuwindow
from passcode_f import passcodewindow
from root_f import rootwindow
from fac_rec_f import fac_recwindow
from start_car_f import start_carwindow
from manage_drivers_f import manage_driverswindow
from name_new_user_f import name_new_userwindow
from cap_new_user_f import cap_new_userwindow
from remove_a_driver_f import remove_a_driverwindow
from trainer_f import trainerwindow
from error_f import errorwindow
from error_fac_rec_f import error_fac_recwindow
from PyQt5.QtCore import QTimer
import subprocess

import os.path
import os
import numpy as np
import numbers
from PIL import Image


#data for training
dataset='dataset/'

# Full screen mode
full_screen = 1
# Default_passcode
my_passcode='1111'
# timer for root menu 60 seconds
timer_for_root=60

app = QApplication(sys.argv)

counter=0

timer_back2main = QTimer()

def timer_process():
    global counter,timer_for_root
    counter=timer_for_root
    # 1 second each
    if not timer_back2main.isActive():
        timer_back2main.start(1000)


def time_handler():
        global counter
        counter -= 1

        if root.isVisible():
            # lcdNumber root
            root.lcdNumber.display(counter)
            # lcdNumber start car
        elif start_car.isVisible():
            start_car.lcdNumber.display(counter)

        #lcdNumber
        if counter <=0:
            timer_back2main.stop()
            back_to_main()




# from passcode_to_root
def open_root():
    passcode.close()
    start_car.close()
    manage_drivers.close()


    if fac_rec.isVisible():
        fac_rec.timer_main.stop()
        fac_rec.close()

    if trainer.isVisible():
        trainer.timer_back2root.stop()
        trainer.close()

    # count down 60 seconds to exitting
    timer_process()


    if full_screen:
        root.showFullScreen()
    else:
        root.show()

#open root by comparing code
def compare_code():
    temp_passcode = passcode.lineEdit.text()
    if my_passcode == temp_passcode:
        open_root()
    else:
        back_to_main()



#from passcode or root to main
def back_to_main():
    #close possible open window
    passcode.close()
    fac_rec.close()
    root.close()
    error_fac_rec.close()



    #check timers and stop them
    if timer_back2main.isActive():
        timer_back2main.stop()


    if fac_rec.timer.isActive():
        fac_rec.timer.stop()
        fac_rec.cap.release()

    if full_screen:
        mainmenu.showFullScreen()
    else:
        mainmenu.show()

#from main to passcode
def open_passcode():
    mainmenu.close()
    passcode.lineEdit.clear()
    if full_screen:
        passcode.showFullScreen()
    else:
        passcode.show()

#from main to facial recognition
def open_fac_rec():

    mainmenu.close()

    # list names in dataset directory
    name_array = os.listdir(dataset)

    if name_array:
        fac_rec.camera_init()
        if full_screen:
            fac_rec.showFullScreen()
        else:
            fac_rec.show()
    else:
        #open error_fac_rec
        open_error_fac_rec()


#==========================================================================================================================
#===================IMPORTANT TURN ON THE CAR RIGHT HERE==================================================================
def open_start_car():
    fac_rec.close()
    passcode.close()
    root.close()
    #count down 60 seconds to exitting
    timer_process()

    if fac_rec.timer.isActive():
        fac_rec.timer.stop()
        fac_rec.cap.release()
    if full_screen:
        start_car.showFullScreen()
    else:
        start_car.show()
#==========================================================================================================================
#==========================================================================================================================
#---------------------------------------------------------------------------------------------------

def open_manage_drivers():
    root.close()
    name_new_user.close()
    cap_new_user.close()
    remove_a_driver.close()
    #check timers and stop them
    if timer_back2main.isActive():
        timer_back2main.stop()

    if cap_new_user.timer3.isActive():
        # stop timer
        cap_new_user.timer3.stop()


    if full_screen:
        manage_drivers.showFullScreen()
    else:
        manage_drivers.show()

def open_name_new_user():
    manage_drivers.close()
    error.close()
    name_new_user.lineEdit.clear()
    if full_screen:
        name_new_user.showFullScreen()
    else:
        name_new_user.show()

def open_cap_new_user(new_name):
    name_new_user.close()
    cap_new_user.new_name = new_name
    cap_new_user.camera_init()
    if full_screen:
        cap_new_user.showFullScreen()
    else:
        cap_new_user.show()

def open_remove_a_driver():
    manage_drivers.close()
    remove_a_driver.remove_f()
    if full_screen:
        remove_a_driver.showFullScreen()
    else:
        remove_a_driver.show()


#open check error before process
def check_error():
    driver_name = name_new_user.lineEdit.text()

    # list names in dataset directory
    name_array = os.listdir(dataset)


    # GUI prompt user to enter their name
    new_name = driver_name


    # GUI new_name valid or invalid
    if (new_name + '\n') in name_array or new_name == '':
        open_error()
    else:
        open_cap_new_user(new_name)


def open_error():
    name_new_user.close()
    if full_screen:
        error.showFullScreen()
    else:
        error.show()


def open_error_fac_rec():
    mainmenu.close()
    if full_screen:
        error_fac_rec.showFullScreen()
    else:
        error_fac_rec.show()


def open_trainer():
    # list names in dataset directory
    name_array = os.listdir(dataset)
    manage_drivers.close()
    if name_array:
        if full_screen:
            trainer.showFullScreen()
        else:
            trainer.show()

        trainer.start()
    else:
        open_root()

#Load the camera setting
subprocess.run(["uvcdynctrl","-L","cam.gpf1"])


#object instantiation
mainmenu = mainmenuwindow()
passcode = passcodewindow()
root = rootwindow()
fac_rec = fac_recwindow()
start_car = start_carwindow()
manage_drivers = manage_driverswindow()
name_new_user = name_new_userwindow()
cap_new_user = cap_new_userwindow()
remove_a_driver = remove_a_driverwindow()
trainer=trainerwindow()
error = errorwindow()
error_fac_rec = error_fac_recwindow()



#start with mainmenu
if full_screen:
    mainmenu.showFullScreen()
else:
    mainmenu.show()

#timer back2main
timer_back2main.timeout.connect(time_handler)
#timer_to_manage_drivers
cap_new_user.timer3.timeout.connect(open_manage_drivers)
trainer.timer_back2root.timeout.connect(open_root)

#button tree
mainmenu.passcode_button.clicked.connect(open_passcode)
mainmenu.facial_button.clicked.connect(open_fac_rec)

passcode.enter_button.clicked.connect(compare_code)
passcode.backtomainmenu_button.clicked.connect(back_to_main)

root.backtomainmenu_button2.clicked.connect(back_to_main)
root.start_car_button.clicked.connect(open_start_car)
root.manage_drivers_button.clicked.connect(open_manage_drivers)


fac_rec.backtomainmenu_button3.clicked.connect(back_to_main)
fac_rec.timer_main.timeout.connect(open_root)

start_car.back_to_root.clicked.connect(open_root)

manage_drivers.add_driver.clicked.connect(open_name_new_user)
manage_drivers.remove_driver.clicked.connect(open_remove_a_driver)
manage_drivers.backtoroot.clicked.connect(open_trainer)

name_new_user.backtomanagedrivers_button.clicked.connect(open_manage_drivers)
name_new_user.benter.clicked.connect(check_error)

remove_a_driver.back.clicked.connect(open_manage_drivers)

error.back.clicked.connect(open_name_new_user)
error_fac_rec.pushButton.clicked.connect(back_to_main)
sys.exit(app.exec_())

