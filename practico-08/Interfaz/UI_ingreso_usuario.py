# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ingreso_usuario.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Otros.utiles import Utiles

class Usuario_encontrado(object):
    def __init__(self, user, ingreso_ok):
        print(user)
        self.user = user
        self.ingreso_ok = ingreso_ok
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(741, 382)
        Dialog.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.btnOk = QtWidgets.QPushButton(Dialog)
        self.btnOk.setGeometry(QtCore.QRect(610, 330, 111, 31))
        self.btnOk.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.btnOk.setObjectName("btnOk")
        self.lblImagen = QtWidgets.QLabel(Dialog)
        self.lblImagen.setGeometry(QtCore.QRect(380, 10, 321, 291))
        self.lblImagen.setText("")
        self.lblImagen.setAlignment(QtCore.Qt.AlignCenter)
        self.lblImagen.setObjectName("lblImagen")
        self.lblNombre = QtWidgets.QLabel(Dialog)
        self.lblNombre.setGeometry(QtCore.QRect(10, 10, 341, 191))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblNombre.setFont(font)
        self.lblNombre.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNombre.setWordWrap(True)
        self.lblNombre.setObjectName("lblNombre")
        self.lblSexo = QtWidgets.QLabel(Dialog)
        self.lblSexo.setGeometry(QtCore.QRect(20, 230, 371, 17))
        self.lblSexo.setObjectName("lblSexo")
        self.lblEdad = QtWidgets.QLabel(Dialog)
        self.lblEdad.setGeometry(QtCore.QRect(20, 310, 381, 17))
        self.lblEdad.setObjectName("lblEdad")
        self.lblDNI = QtWidgets.QLabel(Dialog)
        self.lblDNI.setGeometry(QtCore.QRect(20, 270, 381, 17))
        self.lblDNI.setObjectName("lblDNI")
        self.lblmsg = QtWidgets.QLabel(Dialog)
        self.lblmsg.setGeometry(QtCore.QRect(20, 350, 401, 17))
        self.lblmsg.setObjectName("lblmsg")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.btnOk.clicked.connect(Dialog.close)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ingreso"))
        self.btnOk.setText(_translate("Dialog", "OK"))
        self.lblNombre.setText(_translate("Dialog", self.user._nombre+' '+self.user._apellido))
        if self.user._sexo == 'M':
            self.lblSexo.setText(_translate("Dialog", "Masculino."))
        else:
            self.lblSexo.setText(_translate("Dialog", "Femenino."))
            
        self.lblEdad.setText(_translate("Dialog", 'Edad: '+Utiles.calculaEdad(self.user._fecha_nac)+' años.'))
        self.lblDNI.setText(_translate("Dialog", 'DNI: '+self.user._dni))
        if self.ingreso_ok:
            Dialog.setStyleSheet("background-color:rgb(18, 178, 28);")
            self.lblmsg.setText(_translate("Dialog", "Bienvenido, puede ingresar."))
        else:
            Dialog.setStyleSheet("background-color:rgb(243, 20, 49);")
            self.lblmsg.setText(_translate("Dialog", "Usted no posee la edad suficiente."))

        height, width, channel = self.user._imagen.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(self.user._imagen.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        self.lblImagen.setPixmap(QtGui.QPixmap(qImg))



def mostrar_ingreso_usuario(self,user,ingreso_ok):
    import sys

    self.Dialog = QtWidgets.QMainWindow()
    self.ui = Usuario_encontrado(user,ingreso_ok)
    self.ui.setupUi(self.Dialog)
    self.Dialog.show()
    #sys.exit(persona.exec_())
if __name__ == "__main__":
    mostrar_ingreso_usuario()