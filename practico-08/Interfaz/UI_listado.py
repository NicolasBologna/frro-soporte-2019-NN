# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listado.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_listado(object):
    def __init__(self, ingresos):
        self.ingresos = ingresos

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(754, 583)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 731, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(len(self.ingresos))

        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 200)


        self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Nombre y Apellido"))
        self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("DNI"))
        self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Pudo ingresar?"))
        self.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Fecha"))

        if self.ingresos:
            for id,ingreso in enumerate(self.ingresos):
                print(ingreso)
                self.tableWidget.setItem(id,0,QtWidgets.QTableWidgetItem(ingreso['nombre_apellido']))
                self.tableWidget.setItem(id,1,QtWidgets.QTableWidgetItem(ingreso['dni']))
                ingreso_correcto = 'Si' if ingreso['valido'] else 'No'
                self.tableWidget.setItem(id,2,QtWidgets.QTableWidgetItem(ingreso_correcto))
                self.tableWidget.setItem(id,3,QtWidgets.QTableWidgetItem(ingreso['fecha']))



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Listado de ingresos"))
        self.label.setText(_translate("Dialog", "Lista de ingresos "))
        #self.tableWidget.setItem(self,str('hola'),QtWidgets.QTableWidgetItem)

def mostrar_listado(self,ingresos):
    import sys

    self.Dialog = QtWidgets.QDialog()
    self.ui = Ui_listado(ingresos)
    self.ui.setupUi(self.Dialog)
    self.Dialog.show()


if __name__ == "__main__":
    mostrar_listado()
