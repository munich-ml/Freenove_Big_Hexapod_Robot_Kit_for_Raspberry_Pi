# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Freenove\Desktop\树莓派六足机器人\界面UI\face.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Face(object):
    def setupUi(self, Face):
        Face.setObjectName("Face")
        Face.resize(650, 320)
        Face.setStyleSheet(
            "QWidget{\n"
            "background:#484848;\n"
            "}\n"
            "QAbstractButton{\n"
            "border-style:none;\n"
            "border-radius:0px;\n"
            "padding:5px;\n"
            "color:#DCDCDC;\n"
            "background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #858585,stop:1 #383838);\n"
            "}\n"
            "QAbstractButton:hover{\n"
            "color:#000000;\n"
            "background-color:#008aff;\n"
            "}\n"
            "QAbstractButton:pressed{\n"
            "color:#DCDCDC;\n"
            "border-style:solid;\n"
            "border-width:0px 0px 0px 4px;\n"
            "padding:4px 4px 4px 2px;\n"
            "border-color:#008aff;\n"
            "background-color:#444444;\n"
            "}\n"
            "\n"
            "QLabel{\n"
            "color:#DCDCDC;\n"
            "\n"
            "\n"
            "}\n"
            "QLabel:focus{\n"
            "border:1px solid #00BB9E;\n"
            "\n"
            "}\n"
            "\n"
            "QLineEdit{\n"
            "border:1px solid #242424;\n"
            "border-radius:3px;\n"
            "padding:2px;\n"
            "background:none;\n"
            "selection-background-color:#484848;\n"
            "selection-color:#DCDCDC;\n"
            "}\n"
            "QLineEdit:focus,QLineEdit:hover{\n"
            "border:1px solid #242424;\n"
            "}\n"
            "QLineEdit{\n"
            "border:1px solid #242424;\n"
            "border-radius:3px;\n"
            "padding:2px;\n"
            "background:none;\n"
            "selection-background-color:#484848;\n"
            "selection-color:#DCDCDC;\n"
            "}\n"
            "\n"
            "QLineEdit:focus,QLineEdit:hover{\n"
            "border:1px solid #242424;\n"
            "}\n"
            "QLineEdit{\n"
            "lineedit-password-character:9679;\n"
            "}"
        )
        self.label_video = QtWidgets.QLabel(Face)
        self.label_video.setGeometry(QtCore.QRect(20, 10, 400, 300))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_video.setFont(font)
        self.label_video.setAlignment(QtCore.Qt.AlignCenter)
        self.label_video.setObjectName("label_video")
        self.label_photo = QtWidgets.QLabel(Face)
        self.label_photo.setGeometry(QtCore.QRect(440, 15, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_photo.setFont(font)
        self.label_photo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_photo.setObjectName("label_photo")
        self.lineEdit = QtWidgets.QLineEdit(Face)
        self.lineEdit.setGeometry(QtCore.QRect(490, 235, 140, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Face)
        self.label.setGeometry(QtCore.QRect(440, 240, 45, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Button_Read_Face = QtWidgets.QPushButton(Face)
        self.Button_Read_Face.setGeometry(QtCore.QRect(460, 275, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Button_Read_Face.setFont(font)
        self.Button_Read_Face.setObjectName("Button_Read_Face")

        self.retranslateUi(Face)
        QtCore.QMetaObject.connectSlotsByName(Face)

    def retranslateUi(self, Face):
        _translate = QtCore.QCoreApplication.translate
        Face.setWindowTitle(_translate("Face", "Face"))
        self.label_video.setText(_translate("Face", "Video"))
        self.label_photo.setText(_translate("Face", "Photo"))
        self.label.setText(_translate("Face", "Name:"))
        self.Button_Read_Face.setText(_translate("Face", "Read Face"))
