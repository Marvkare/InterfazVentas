import json
import os

path,_ = os.path.split(os.path.abspath(__file__))
path,__ = path.split('Controllers')
print(path)
data={}

def guardarDataJson(): 
        with open(path+"data.json", 'w') as file:
            json.dump(data,file, indent=4)

def loadData():
        with open(path+'data.json') as file:
            data = json.load(file)

        if len(data) == 0 : 
            data['Productos'] = []
            data['Ventas'] =[]
            data['Usuario'] =[]
            guardarDataJson()
        return data
