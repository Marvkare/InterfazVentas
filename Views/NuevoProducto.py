from PyQt5 import uic, QtWidgets, QtGui
import json
import os

path,_ = os.path.split(os.path.abspath(__file__))
path,__= path.split('Views')
Ui_NuevoProducto, QtBasesClass = uic.loadUiType("Views/InventarioVentana.ui")

class NuevoProducto(QtWidgets.QMainWindow, Ui_NuevoProducto):

    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        Ui_NuevoProducto.__init__(self)
        self.setupUi(self)
        self.pushButtonAgregarProducto.clicked.connect(lambda: self.getData())
        self.data = {}
        self.loadData()
        self.writeTable()

    def getData(self):
        nombreProducto = self.lineEditNameProduct.text()
        descripcionProducto = self.lineEditDescripcion.text()
        precioProducto = int(self.lineEditPrecio.text())
        cantidadProducto = int(self.lineEditCantidad.text())
        print(self.data)
        self.data['Productos'].append({
                    'nombre_Producto': nombreProducto,
                    'descripcion_Producto': descripcionProducto,
                    'precio_Producto': precioProducto,
                    'cantidad_Producto': cantidadProducto
                })
        self.guardarDataJson()
        self.writeTable()
        


    def guardarDataJson(self): 
        with open(path+"data.json", 'w') as file:
            json.dump(self.data,file, indent=4)
    
    
    def loadData(self):
        with open(path+'data.json') as file:
            self.data = json.load(file)

        if len(self.data) == 0 : 
            self.data['Productos'] = []
            self.data['Ventas'] =[]
            self.data['Usuario'] =[]
            self.guardarDataJson()
            

    def writeTable(self):
        row =0 
        self.tableWidget.setRowCount(len(self.data['Productos']))
        for item in self.data['Productos']:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(item['nombre_Producto']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(item['descripcion_Producto']))           
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem('$'+str(item['precio_Producto'])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(item['cantidad_Producto'])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem())
            row = row +1
            print(item)
   s 