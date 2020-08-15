# The first project i am going to do :)
# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.14.0
#====================================mouduls=====================================
from PyQt5 import QtCore, QtGui, QtWidgets
import random
#====================================QP designer================================
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 177)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exe = QtWidgets.QPushButton(self.centralwidget)
        self.exe.setGeometry(QtCore.QRect(140, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exe.setFont(font)
        self.exe.setObjectName("exe")
        self.dis_password = QtWidgets.QTextBrowser(self.centralwidget)
        self.dis_password.setGeometry(QtCore.QRect(80, 50, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.dis_password.setFont(font)
        self.dis_password.setObjectName("dis_password")
        self.dis_message = QtWidgets.QTextBrowser(self.centralwidget)
        self.dis_message.setGeometry(QtCore.QRect(0, 0, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Pacifico")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.dis_message.setFont(font)
        self.dis_message.setFrameShape(QtWidgets.QFrame.Box)
        self.dis_message.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dis_message.setObjectName("dis_message")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exe.clicked.connect(self.Random)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#===================================base syntax=================================
    def Random(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        length = 8
        new_password = ""

        for i in range(length):
            next_index = random.randrange(len(alphabet))
            new_password = new_password + alphabet[next_index]


        for i in range(random.randrange(1,3)):
            replace_index = random.randrange(len(new_password)//2)
            new_password = new_password[0:replace_index] + str(random.randrange(10)) + new_password[replace_index+1:]


        for i in range(random.randrange(1,3)):
            replace_index = random.randrange(len(new_password)//2,len(new_password))
            new_password = new_password[0:replace_index] + new_password[replace_index].upper() + new_password[replace_index+1:]

        self.dis_password.setText(new_password);
#==================================other QT designer================================    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exe.setText(_translate("MainWindow", "Run"))
        self.dis_password.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:22pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.dis_message.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Pacifico\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MV Boli\';\">password maker - by mahdi_prhsn</span></p></body></html>"))
#=====================================MAIN=======================================

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
