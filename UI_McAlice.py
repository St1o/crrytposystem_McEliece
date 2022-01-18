# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from Encrypt import *
from Decrypt import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 710)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -260, 750, 460))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:/Downloads/apGl6nEkjY0.jpg"))
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-6, 180, 760, 512))
        font = QtGui.QFont()
        font.setFamily("Euclid Math Two")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 721, 471))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("E:/Downloads/QtzVivBOvYs.png"))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setGeometry(QtCore.QRect(50, 20, 290, 30))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.tab_1)
        self.pushButton.setGeometry(QtCore.QRect(100, 70, 140, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        font.setUnderline(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_1)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 140, 640, 290))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_9 = QtWidgets.QLabel(self.tab_1)
        self.label_9.setGeometry(QtCore.QRect(400, 20, 221, 30))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        font.setUnderline(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 70, 140, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        font.setUnderline(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 761, 471))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("E:/Downloads/QtzVivBOvYs.png"))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(50, 20, 290, 30))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        font.setUnderline(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 70, 140, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        font.setUnderline(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(40, 140, 640, 290))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(400, 20, 221, 30))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        font.setUnderline(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 70, 140, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        font.setUnderline(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 70, 450, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(54, 41, 27, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 690, 721, 20))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)

        def encrypt(self):
            try:
                filename = QFileDialog.getOpenFileName()[0]
                self.plainTextEdit.appendPlainText(create_abstract_text(filename))
            except:
                pass

        def decrypt(self):
            self.plainTextEdit_2.appendPlainText(preparation_decrypt_procedure())

        def choose_directory(self):
            try:
                global path
                path = QFileDialog.getExistingDirectory()
                print(path)
                os.chdir(path)
            except:
                pass

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.pushButton.clicked.connect(lambda: encrypt(self))
        self.pushButton_2.clicked.connect(lambda: decrypt(self))
        self.pushButton_3.clicked.connect(lambda: choose_directory(self))
        self.pushButton_4.clicked.connect(lambda: choose_directory(self))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "McEliece cryptosystem"))
        self.label_5.setText(_translate("MainWindow", "Open file and encrypt"))
        self.pushButton.setText(_translate("MainWindow", "Encrypt"))
        self.label_9.setText(_translate("MainWindow", "Choose directory"))
        self.pushButton_4.setText(_translate("MainWindow", "Path"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "SENDER"))
        self.label_6.setText(_translate("MainWindow", "Open file and decrypt"))
        self.pushButton_2.setText(_translate("MainWindow", "Decrypt"))
        self.label_7.setText(_translate("MainWindow", "Choose directory"))
        self.pushButton_3.setText(_translate("MainWindow", "Path"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "RECIEVER"))
        self.label_4.setText(_translate("MainWindow", "McEliece cryptosystem"))
        self.label_8.setText(_translate("MainWindow", "                                          By Stio"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
