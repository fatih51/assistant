# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Güçlü/Desktop/EBA CANLI DERS FATİH İÇİN İNDİRİLENLER/BİLGİSAYAR/PyQt5 Arayüz Tasarımı/Sesli Asistan/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Main_Frame = QtWidgets.QFrame(self.centralwidget)
        self.Main_Frame.setGeometry(QtCore.QRect(-10, 0, 1011, 801))
        self.Main_Frame.setStyleSheet("#Main_Frame{\n"
"    background-color:rgb(28, 145, 145)\n"
"}")
        self.Main_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main_Frame.setObjectName("Main_Frame")
        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(10, 0, 671, 201))
        self.label_1.setStyleSheet("font-size:25px;\n"
"color:white;")
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.Main_Frame)
        self.lineEdit_1.setGeometry(QtCore.QRect(80, 490, 661, 101))
        self.lineEdit_1.setStyleSheet("border:3px solid;\n"
"border-radius:40px;\n"
"padding-left:200px;\n"
"font-size:20px;\n"
"color:black;\n"
"\n"
"")
        self.lineEdit_1.setText("")
        self.lineEdit_1.setPlaceholderText("")
        self.lineEdit_1.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_1.setClearButtonEnabled(True)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_2 = QtWidgets.QLabel(self.Main_Frame)
        self.label_2.setGeometry(QtCore.QRect(15, 200, 701, 161))
        self.label_2.setStyleSheet("font-size:25px;\n"
"color:white;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Main_Frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 590, 661, 101))
        self.lineEdit_2.setStyleSheet("border:3px solid;\n"
"border-radius:40px;\n"
"font-size:16px;\n"
"color:black;\n"
"\n"
"")
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jarvis"))
        self.lineEdit_1.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>A</p></body></html>"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Burası Arama,Youtube,Wikpedia,Müzik ve Hava Fonksiyonuna cevap vereceğiniz kısımdır"))

