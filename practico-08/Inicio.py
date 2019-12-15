# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from Negocio.neg_Main import Reconocimiento

from Negocio.neg_ingresos import Ingresos
#from dialog1 import ejecuta_d1
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

from Interfaz.UI_ingreso_usuario import mostrar_ingreso_usuario
from Interfaz.UI_listado import mostrar_listado

import imagen.Resources_rc

class Ui_MainWindow(object):
    def __init__(self):
      self.contador_cant_ingresos = 0
      
    def setupUi(self, MainWindow):
      MainWindow.setObjectName("MainWindow")
      MainWindow.resize(1280, 650)
      sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
      sizePolicy.setHorizontalStretch(0)
      sizePolicy.setVerticalStretch(0)
      sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
      MainWindow.setSizePolicy(sizePolicy)
      MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
      MainWindow.setAutoFillBackground(False)
      MainWindow.setStyleSheet("QWidget#centralwidget\n"
"{\n"
"    background-image: url(:/prueba/costello.jpeg);\n"
"}")
      self.centralwidget = QtWidgets.QWidget(MainWindow)
      sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
      sizePolicy.setHorizontalStretch(0)
      sizePolicy.setVerticalStretch(0)
      sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
      self.centralwidget.setSizePolicy(sizePolicy)
      self.centralwidget.setAutoFillBackground(False)
      self.centralwidget.setStyleSheet("")
      self.centralwidget.setObjectName("centralwidget")
      self.lblContador = QtWidgets.QLabel(self.centralwidget)
      self.lblContador.setGeometry(QtCore.QRect(1200, 70, 67, 17))
      self.lblContador.setStyleSheet("color: rgb(238, 238, 236);")
      self.lblContador.setObjectName("lblContador")
      self.lblContadorText = QtWidgets.QLabel(self.centralwidget)
      self.lblContadorText.setGeometry(QtCore.QRect(1130, 70, 71, 17))
      self.lblContadorText.setStyleSheet("color: rgb(255, 255, 255);")
      self.lblContadorText.setObjectName("lblContadorText")
      self.lblTitulo = QtWidgets.QLabel(self.centralwidget)
      self.lblTitulo.setGeometry(QtCore.QRect(360, -10, 611, 111))
      sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
      sizePolicy.setHorizontalStretch(0)
      sizePolicy.setVerticalStretch(0)
      sizePolicy.setHeightForWidth(self.lblTitulo.sizePolicy().hasHeightForWidth())
      self.lblTitulo.setSizePolicy(sizePolicy)
      self.lblTitulo.setStyleSheet("background-color: rgb(255, 255, 255,0%);\n"
"font: 75 61pt \"URW Bookman L\";\n"
"color: rgb(255, 255, 255);\n"
"text-shadow: -5px 5 red, 0 5px black, 5px 0 black, 0 -5px black;\n"
"")
      self.lblTitulo.setObjectName("lblTitulo")
      self.BotonIngreso = QtWidgets.QPushButton(self.centralwidget)
      self.BotonIngreso.setGeometry(QtCore.QRect(400, 175, 551, 191))
      font = QtGui.QFont()
      font.setFamily("Ebrima")
      font.setPointSize(20)
      self.BotonIngreso.setFont(font)
      self.BotonIngreso.setMouseTracking(True)
      self.BotonIngreso.setAutoFillBackground(False)
      self.BotonIngreso.setStyleSheet("background-color: rgb(78, 154, 6);\n"
"")
      self.BotonIngreso.setAutoDefault(True)
      self.BotonIngreso.setDefault(True)
      self.BotonIngreso.setFlat(False)
      self.BotonIngreso.setObjectName("BotonIngreso")



      self.BotonListado = QtWidgets.QPushButton(self.centralwidget)
      self.BotonListado.setGeometry(QtCore.QRect(400, 390, 551, 130))
      self.BotonListado.setFont(font)
      self.BotonListado.setMouseTracking(True)
      self.BotonListado.setAutoFillBackground(False)
      self.BotonListado.setStyleSheet("background-color: rgb(134, 124, 36);\n"
"")
      self.BotonListado.setAutoDefault(True)
      self.BotonListado.setDefault(True)
      self.BotonListado.setFlat(False)
      self.BotonListado.setObjectName("BotonListado")

      

      self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
      self.btnSalir.setGeometry(QtCore.QRect(1160, 560, 89, 25))
      self.btnSalir.setStyleSheet("background-color: rgb(204, 0, 0);")
      self.btnSalir.setObjectName("btnSalir")
      MainWindow.setCentralWidget(self.centralwidget)
      self.menubar = QtWidgets.QMenuBar(MainWindow)
      self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
      self.menubar.setObjectName("menubar")
      MainWindow.setMenuBar(self.menubar)
      self.statusbar = QtWidgets.QStatusBar(MainWindow)
      self.statusbar.setObjectName("statusbar")
      MainWindow.setStatusBar(self.statusbar)

      self.retranslateUi(MainWindow)
      QtCore.QMetaObject.connectSlotsByName(MainWindow)

      self.btnSalir.clicked.connect(QtCore.QCoreApplication.instance().quit)

      self.BotonIngreso.clicked.connect(self.ingreso)
      self.BotonListado.clicked.connect(self.listado)

    def listado(self):
      mostrar_listado(self,Ingresos.traerIngresos())

    def ingreso(self):
      user,ingreso_ok = reconocimiento.reconocer()
      
      mostrar_ingreso_usuario(self,user,ingreso_ok)
      if ingreso_ok:
        self.contador_cant_ingresos +=1
      self.retranslateUi(MainWindow)


    def retranslateUi(self, MainWindow):
      _translate = QtCore.QCoreApplication.translate
      MainWindow.setWindowTitle(_translate("MainWindow", "Reconociendote"))
      self.lblContador.setText(_translate("MainWindow", str(self.contador_cant_ingresos)))
      self.lblContadorText.setText(_translate("MainWindow", "Ingresos:"))
      self.lblTitulo.setText(_translate("MainWindow", "Costello Oficial"))
      self.BotonIngreso.setText(_translate("MainWindow", "Ingreso"))
      self.BotonListado.setText(_translate("MainWindow", "Listado ingresos"))
      self.btnSalir.setText(_translate("MainWindow", "Salir"))



if __name__ == "__main__":
    import sys
    
    reconocimiento = Reconocimiento()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()    
    sys.exit(app.exec_())
