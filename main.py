from PyQt5 import QtCore
from PyQt5.QtWidgets import*
from ui_splash_screen_2 import Ui_SplashScreen #burada 'notlar' kısmı ui dosyasının py olmuş hali olacak

counter = 0



class a(QMainWindow,Ui_SplashScreen):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.b)

        self.timer.start(35)

    def b(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()
            self.close()
            
        counter += 1


      
        
        

uygulama = QApplication([])
pencere = a()
pencere.show()
uygulama.exec_()
