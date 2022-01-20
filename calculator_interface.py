# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(241, 274)
        MainWindow.setStyleSheet("background-color: #22222e")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 60, 71, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid #f66867;")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 211, 61))
        self.lineEdit.setStyleSheet("font: italic 16pt \"MS Serif\";\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Nirmala UI\";\n"
"border: 2px solid #f66867;")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 60, 71, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid #f66867;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 60, 71, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid #f66867;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 100, 71, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid #f66867;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 100, 71, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid #f66867;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 100, 71, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid #f66867;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 140, 71, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid #f66867;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 140, 71, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid #f66867;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(140, 140, 71, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid #f66867;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(70, 180, 71, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid #f66867;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(210, 60, 31, 41))
        self.pushButton_11.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"border: 2px solid #f66867;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(210, 100, 31, 41))
        self.pushButton_12.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"border: 2px solid #f66867;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(140, 180, 71, 41))
        self.pushButton_13.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"border: 2px solid #f66867;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(210, 180, 31, 41))
        self.pushButton_14.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"border: 2px solid #f66867;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(210, 140, 31, 41))
        self.pushButton_15.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"border: 2px solid #f66867;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(0, 180, 71, 41))
        self.pushButton_16.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"background-color: rgb(255, 0, 0);\n"
"border: 2px solid #f66867;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(210, 0, 31, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"background-color: rgb(255, 0, 0);\n"
"border: 2px solid #f66867;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(0, 220, 61, 31))
        self.pushButton_18.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"border: 2px solid #f66867;")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(60, 220, 61, 31))
        self.pushButton_19.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"border: 2px solid #f66867;")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(120, 220, 61, 31))
        self.pushButton_20.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"border: 2px solid #f66867;")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(180, 220, 61, 31))
        self.pushButton_21.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"border: 2px solid #f66867;")
        self.pushButton_21.setObjectName("pushButton_21")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.lineEdit.setText(_translate("MainWindow", "             CALCULATOR"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_10.setText(_translate("MainWindow", "0"))
        self.pushButton_11.setText(_translate("MainWindow", "+"))
        self.pushButton_12.setText(_translate("MainWindow", "-"))
        self.pushButton_13.setText(_translate("MainWindow", "="))
        self.pushButton_14.setText(_translate("MainWindow", "/"))
        self.pushButton_15.setText(_translate("MainWindow", "*"))
        self.pushButton_16.setText(_translate("MainWindow", "C"))
        self.pushButton_17.setText(_translate("MainWindow", "EXIT"))
        self.pushButton_18.setText(_translate("MainWindow", "("))
        self.pushButton_19.setText(_translate("MainWindow", ")"))
        self.pushButton_20.setText(_translate("MainWindow", "%"))
        self.pushButton_21.setText(_translate("MainWindow", "."))
