from PyQt5 import uic, QtWidgets
#------- Manejo de interfazes
from Views.VistaPrincipal import VentanaInicio



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = VentanaInicio()
    window.show()
    app.exec()