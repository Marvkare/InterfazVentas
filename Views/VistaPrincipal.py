import sys
from random import randint
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget

#--------Importamos interfazes de clases externas 
from Views.NuevaVenta import NuevaVenta

from Views.NuevoProducto import NuevoProducto

#------Importamos el archivo Ui  y cargamos el archivo---------
qtCreatorFile = "Views/Main.ui"
Ui_MainWindow, QtBasesClass = uic.loadUiType(qtCreatorFile)
#--------clase principar
class VentanaInicio(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #-------Cargamos nuestra interfaz
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        # 
        self.setupUi(self)
        


        self.inventario_Button.clicked.connect(lambda: self.NuevoProducto())
        self.nuevaVenta_Button.clicked.connect(lambda: self.NuevaVenta())


    
    def NuevoProducto(self):
        self.window=NuevoProducto()
        self.window.show()
    def NuevaVenta(self):
        self.window=NuevaVenta()
        self.window.show()


