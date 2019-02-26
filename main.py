# Phong Nguyen
# ECE 412, Winter 2019
# Capstone Project: Anti-theft and Collision detection


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
from error_f import errorwindow
from PyQt5.QtCore import QTimer


import os.path
import os
import numpy as np
import numbers
from PIL import Image



#save.txt
save_path='save.txt'

# Full screen mode
full_screen = 0
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
    # count down 60 seconds to exitting
    timer_process()

    if fac_rec.isVisible():
        fac_rec.timer_main.stop()
        fac_rec.close()

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
    fac_rec.camera_init()
    mainmenu.close()
    if full_screen:
        fac_rec.showFullScreen()
    else:
        fac_rec.show()
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

def open_cap_new_user(Id):
    name_new_user.close()
    cap_new_user.Id=Id
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

    name_array = []
    # open save.txt
    if os.path.isfile(save_path):
        with open(save_path, 'r+') as my_file:
            name_array = my_file.readlines()

        # GUI prompt user to enter their name
    new_name = driver_name


    # GUI new_name valid or invalid
    if (new_name + '\n') in name_array or new_name == '':
        open_error()
    else:
        # write new name to file
        my_file = open(save_path, 'a+')
        my_file.write(new_name + '\n')
        my_file.close()

        # add new name to the end of the list
        name_array.append(new_name)

        # id base on position in name array. 0 dont count
        Id = len(name_array)


        open_cap_new_user(Id)


def open_error():
    name_new_user.close()
    if full_screen:
        error.showFullScreen()
    else:
        error.show()




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
error = errorwindow()



#start with mainmenu
if full_screen:
    mainmenu.showFullScreen()
else:
    mainmenu.show()

#timer back2main
timer_back2main.timeout.connect(time_handler)
#timer_to_manage_drivers
cap_new_user.timer3.timeout.connect(open_manage_drivers)

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
manage_drivers.backtoroot.clicked.connect(open_root)

name_new_user.backtomanagedrivers_button.clicked.connect(open_manage_drivers)
name_new_user.benter.clicked.connect(check_error)

remove_a_driver.back.clicked.connect(open_manage_drivers)

error.back.clicked.connect(open_name_new_user)
sys.exit(app.exec_())

