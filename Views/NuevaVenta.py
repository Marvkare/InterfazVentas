from PyQt5 import  uic, QtWidgets
from Views.ListaProductos import ListaProductos
from Controllers.jsonController import guardarDataJson,loadData
Ui_BProducto, QtBasesClassBp = uic.loadUiType("Views/NuevaVenta.ui")

class NuevaVenta(QtWidgets.QMainWindow, Ui_BProducto):
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        Ui_BProducto.__init__(self)
        self.setupUi(self)     
        self.data = loadData()
        self.mostrarDataTabla()
        

    def mostrarDataTabla(self):
        row =0 
        self.tableWidget.setRowCount(len(self.data['Productos']))
        for item in self.data['Productos']:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(item['nombre_Producto']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(item['descripcion_Producto']))           
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem('$'+str(item['precio_Producto'])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(item['cantidad_Producto'])))
            row = row +1
            print(item) 