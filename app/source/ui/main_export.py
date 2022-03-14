# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_export.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 391)
        MainWindow.setMinimumSize(QtCore.QSize(351, 391))
        MainWindow.setMaximumSize(QtCore.QSize(351, 391))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_select_path = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_select_path.setGeometry(QtCore.QRect(10, 20, 231, 22))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_select_path.setFont(font)
        self.lineEdit_select_path.setObjectName("lineEdit_select_path")
        self.pushButton_select_path = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_select_path.setGeometry(QtCore.QRect(250, 20, 71, 23))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_select_path.setFont(font)
        self.pushButton_select_path.setObjectName("pushButton_select_path")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 80, 161, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.spinBox_start_count = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_start_count.setGeometry(QtCore.QRect(40, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_start_count.setFont(font)
        self.spinBox_start_count.setMaximum(9999999)
        self.spinBox_start_count.setObjectName("spinBox_start_count")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 250, 331, 111))
        font = QtGui.QFont()
        font.setFamily("等线")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_start_mp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start_mp.setGeometry(QtCore.QRect(20, 150, 91, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_mp.setFont(font)
        self.pushButton_start_mp.setObjectName("pushButton_start_mp")
        self.pushButton_start_spec = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start_spec.setGeometry(QtCore.QRect(130, 150, 91, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_spec.setFont(font)
        self.pushButton_start_spec.setObjectName("pushButton_start_spec")
        self.pushButton_start_bridge = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start_bridge.setGeometry(QtCore.QRect(240, 150, 91, 61))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start_bridge.setFont(font)
        self.pushButton_start_bridge.setObjectName("pushButton_start_bridge")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 220, 331, 21))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_info = QtWidgets.QLabel(self.groupBox_3)
        self.label_info.setGeometry(QtCore.QRect(0, 0, 331, 20))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setBold(True)
        font.setWeight(75)
        self.label_info.setFont(font)
        self.label_info.setText("")
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.checkBox_skip_2_4_bridge = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_skip_2_4_bridge.setGeometry(QtCore.QRect(190, 100, 121, 21))
        self.checkBox_skip_2_4_bridge.setObjectName("checkBox_skip_2_4_bridge")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "7600_TXT_2_EXCEL"))
        self.groupBox.setTitle(_translate("MainWindow", "选择TXT文件所在文件夹"))
        self.pushButton_select_path.setText(_translate("MainWindow", "选择路径"))
        self.groupBox_2.setTitle(_translate("MainWindow", "起始数量"))
        self.pushButton_start_mp.setText(_translate("MainWindow", "生成MP"))
        self.pushButton_start_spec.setText(_translate("MainWindow", "生成SPEC"))
        self.pushButton_start_bridge.setText(_translate("MainWindow", "生成Bridge"))
        self.checkBox_skip_2_4_bridge.setText(_translate("MainWindow", "跳过2.4G Bridge"))
