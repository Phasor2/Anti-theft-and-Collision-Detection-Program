#Phong Nguyen
#ECE 412, Winter 2019
#Capstone Project: Anti-theft and Collision detection


import sys
from PyQt5.QtWidgets import QApplication
from mainmenu_f import mainmenuwindow
from passcode_f import passcodewindow
from root_f import rootwindow
from fac_rec_f import fac_recwindow
from start_car_f import start_carwindow
from PyQt5.QtCore import QTimer

#Full screen mode
full_screen = 0
#Default_passcode
my_passcode='1111'
#timer for root menu 60 seconds
timer_for_root=60

app = QApplication(sys.argv)

counter=0

timer_back2main = QTimer()

def timer_process():
    global counter,timer_for_root
    counter=timer_for_root
    #1 second each
    if not timer_back2main.isActive():
        timer_back2main.start(1000)


def time_handler():
        global counter
        counter -= 1

        #lcdNumber root
        root.lcdNumber.display(counter)
        #lcdNumber start car

        #lcdNumber
        if counter <=0:
            timer_back2main.stop()
            back_to_main()




#from passcode to root
def open_root():
    passcode.close()
    #count down 60 seconds to exitting
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

#===================IMPORTANT TURN ON THE CAR RIGHT HERE=====================
def open_start_car():
    fac_rec.close()
    passcode.close()
    root.close()
    if fac_rec.timer.isActive():
        fac_rec.timer.stop()
        fac_rec.cap.release()
    if full_screen:
        start_car.showFullScreen()
    else:
        start_car.show()



#---------------------------------------------------------------------------------------------------
#object instantiation
mainmenu = mainmenuwindow()
passcode =  passcodewindow()
root = rootwindow()
fac_rec = fac_recwindow()
start_car = start_carwindow()


#start with mainmenu
if full_screen:
    mainmenu.showFullScreen()
else:
    mainmenu.show()

#time back2main
timer_back2main.timeout.connect(time_handler)

#button tree
mainmenu.passcode_button.clicked.connect(open_passcode)
mainmenu.facial_button.clicked.connect(open_fac_rec)

passcode.enter_button.clicked.connect(compare_code)
passcode.backtomainmenu_button.clicked.connect(back_to_main)

root.backtomainmenu_button2.clicked.connect(back_to_main)
root.start_car_button.clicked.connect(open_start_car)


fac_rec.backtomainmenu_button3.clicked.connect(back_to_main)
fac_rec.timer_main.timeout.connect(open_root)

start_car.back_to_main.clicked.connect(back_to_main)

sys.exit(app.exec_())

