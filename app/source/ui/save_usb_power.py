# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_usb_power.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_save_usb_power(object):
    def setupUi(self, Dialog_save_usb_power):
        Dialog_save_usb_power.setObjectName("Dialog_save_usb_power")
        Dialog_save_usb_power.resize(320, 240)
        self.lineEdit_a = QtWidgets.QLineEdit(Dialog_save_usb_power)
        self.lineEdit_a.setGeometry(QtCore.QRect(110, 100, 91, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_a.setFont(font)
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.lineEdit_v = QtWidgets.QLineEdit(Dialog_save_usb_power)
        self.lineEdit_v.setGeometry(QtCore.QRect(110, 38, 91, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_v.setFont(font)
        self.lineEdit_v.setText("")
        self.lineEdit_v.setObjectName("lineEdit_v")
        self.label = QtWidgets.QLabel(Dialog_save_usb_power)
        self.label.setGeometry(QtCore.QRect(50, 50, 51, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_save_usb_power)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 51, 16))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_save = QtWidgets.QPushButton(Dialog_save_usb_power)
        self.pushButton_save.setGeometry(QtCore.QRect(120, 190, 75, 23))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.label_3 = QtWidgets.QLabel(Dialog_save_usb_power)
        self.label_3.setGeometry(QtCore.QRect(220, 110, 31, 16))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog_save_usb_power)
        self.label_4.setGeometry(QtCore.QRect(220, 50, 31, 21))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog_save_usb_power)
        self.label_5.setGeometry(QtCore.QRect(70, 150, 161, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog_save_usb_power)
        QtCore.QMetaObject.connectSlotsByName(Dialog_save_usb_power)

    def retranslateUi(self, Dialog_save_usb_power):
        _translate = QtCore.QCoreApplication.translate
        Dialog_save_usb_power.setWindowTitle(_translate("Dialog_save_usb_power", "Dialog"))
        self.lineEdit_a.setText(_translate("Dialog_save_usb_power", "0.5"))
        self.label.setText(_translate("Dialog_save_usb_power", "Voltage"))
        self.label_2.setText(_translate("Dialog_save_usb_power", "Current"))
        self.pushButton_save.setText(_translate("Dialog_save_usb_power", "Save"))
        self.label_3.setText(_translate("Dialog_save_usb_power", "A"))
        self.label_4.setText(_translate("Dialog_save_usb_power", "V"))
