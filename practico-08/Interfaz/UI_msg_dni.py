# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msg_dni.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mensaje_dni(object):
    def __init__(self,imagen):
        self.imagen = imagen
    def setupUi(self, Mensaje_dni):
        Mensaje_dni.setObjectName("Mensaje_dni")
        Mensaje_dni.resize(392, 587)
        self.btn_ok = QtWidgets.QPushButton(Mensaje_dni)
        self.btn_ok.setGeometry(QtCore.QRect(150, 550, 89, 25))
        self.btn_ok.setStyleSheet("background-color: rgb(78, 154, 6);\n"
"color: rgb(0, 0, 0);")
        self.btn_ok.setObjectName("btn_ok")
        self.lbl_texto = QtWidgets.QLabel(Mensaje_dni)
        self.lbl_texto.setGeometry(QtCore.QRect(20, 30, 351, 181))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_texto.setFont(font)
        self.lbl_texto.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_texto.setWordWrap(True)
        self.lbl_texto.setObjectName("lbl_texto")
        self.lbl_image_nueva_persona = QtWidgets.QLabel(Mensaje_dni)
        self.lbl_image_nueva_persona.setGeometry(QtCore.QRect(10, 220, 371, 291))
        self.lbl_image_nueva_persona.setText("")
        self.lbl_image_nueva_persona.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_image_nueva_persona.setObjectName("lbl_image_nueva_persona")

        self.retranslateUi(Mensaje_dni)
        QtCore.QMetaObject.connectSlotsByName(Mensaje_dni)

        self.btn_ok.clicked.connect(Mensaje_dni.close)

    def retranslateUi(self, Mensaje_dni):
        _translate = QtCore.QCoreApplication.translate
        Mensaje_dni.setWindowTitle(_translate("Mensaje_dni", "Dialog"))
        self.btn_ok.setText(_translate("Mensaje_dni", "OK"))
        self.lbl_texto.setText(_translate("Mensaje_dni", "Por favor, acerque el código QR del dni de la siguiente persona a la cámara"))
        

        height, width, channel = self.imagen.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(self.imagen.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        self.lbl_image_nueva_persona.setPixmap(QtGui.QPixmap(qImg))

def mostrar_msg_dni(self, imagen):
    import sys

    self.Dialog = QtWidgets.QDialog()
    self.ui = Ui_Mensaje_dni(imagen)
    self.ui.setupUi(self.Dialog)
    self.Dialog.show()
    self.Dialog.move(1400,50)


if __name__ == "__main__":
    mostrar_msg_dni()
