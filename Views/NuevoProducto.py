from PyQt5 import uic, QtWidgets, QtGui
import json
import os
import datetime

path,_ = os.path.split(os.path.abspath(__file__))
path,__= path.split('Views')
Ui_NuevoProducto, QtBasesClass = uic.loadUiType("Views/InventarioVentana.ui")

class NuevoProducto(QtWidgets.QMainWindow, Ui_NuevoProducto):

    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        Ui_NuevoProducto.__init__(self)
        self.setupUi(self)
        self.pushButtonAgregarProducto.clicked.connect(lambda: self.agregarProducto())
        self.data = {}
        self.loadData()
        self.writeTable()
        self.pushButtonEliminar.clicked.connect(lambda: self.eliminarProducto())
        self.pushButtonEditar.clicked.connect(lambda: self.editarProducto())
        self.pushButtonActualizar.clicked.connect(lambda: self.actualizarProducto())
        self.editmode= False
        self.id_random = ''
    def getData(self):
        if self.editmode == False:
            x = datetime.datetime.now()
            self.id_random= str(id(x.second))
        nombreProducto = self.lineEditNameProduct.text()
        descripcionProducto = self.lineEditDescripcion.text()
        precioProducto = int(self.lineEditPrecio.text())
        cantidadProducto = int(self.lineEditCantidad.text())
        data={      'id_Producto':self.id_random,
                    'nombre_Producto': nombreProducto,
                    'descripcion_Producto': descripcionProducto,
                    'precio_Producto': precioProducto,
                    'cantidad_Producto': cantidadProducto
                }
        return data
        
    def agregarProducto(self):
        self.data['Productos'].append(self.getData())
        self.guardarDataJson()
        self.writeTable()
        self.clearEditText()

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
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(item['id_Producto']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(item['nombre_Producto']))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(item['descripcion_Producto']))           
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem('$'+str(item['precio_Producto'])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(item['cantidad_Producto'])))
            row = row +1
    def eliminarProducto(self):
        text = self.lineEditEliminar.text()
        if text :
            newData = []
            for item in self.data['Productos']:
                if item["id_Producto"] != text:
                    newData.append(item)
                    self.labelMensaje.setText("Se elimino el Producto: "+text)

            self.data['Productos']= newData
            self.guardarDataJson()
            self.writeTable()           
        else:
            self.labelError.setText("No haz ingresado ningo numero de producto")
    
    def editarProducto(self):
        text = self.lineEditEliminar.text()
        if text :
            for item in self.data['Productos']:
                if item["id_Producto"] == text:
                    self.lineEditNameProduct.setText(item['nombre_Producto'])
                    self.lineEditDescripcion.setText(item['descripcion_Producto'])
                    self.lineEditPrecio.setText(str(item['precio_Producto']))
                    self.lineEditCantidad.setText(str(item['cantidad_Producto']))
                    self.labelMensaje.setText("Se añadio a edicion el produto: "+text)
        else:
            self.labelError.setText("No haz ingresado ningo numero de producto")
    
    def actualizarProducto(self):
        self.editmode = True
        text = self.lineEditEliminar.text()
        self.id_random = text
        newProducto = self.getData()
        newData =[ ]
        print(newProducto['nombre_Producto'])
        for producto in self.data['Productos']:
            if producto['id_Producto'] != text:
                newData.append(producto)
        newData.append(newProducto)
        self.data['Productos'] = newData 
        self.editmode = False
        self.guardarDataJson()
        self.writeTable()
        self.clearEditText()
    def clearEditText(self):
        self.lineEditNameProduct.setText("")
        self.lineEditDescripcion.setText("")
        self.lineEditPrecio.setText("")
        self.lineEditCantidad.setText("")