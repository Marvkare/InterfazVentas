from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget

#--------Importamos interfazes de clases externas 

#------Importamos el archivo Ui  y cargamos el archivo---------
qtCreatorFile = "Views/Main.ui"
ui_ListaProductos, QtBasesClass = uic.loadUiType(qtCreatorFile)
#--------clase principar

class ListaProductos(QtWidgets.QMainWindow, ui_ListaProductos):

    def __init__(self) -> None:
        super().__init__()
        QtWidgets.QMainWindow().__init__(self)
        ui_ListaProductos.__init_(self)
        self.setupUi(self)