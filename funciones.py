from listas import Listas
import json
class Funciones(Listas):
    def __init__(self, nombre = None, clasificacion =None, director =None, genero =None, año =None):
        if nombre == None:
             super().__init__(True)
        else:
             super().__init__(False)
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.director = director
        self.genero = genero
        self.año = año
        


    def __str__(self):
        if self.lista:
            return str(self.elementos)+ " son el numero de funciones que hay en la lista"
        return f"La funcions {self.nombre} es de clasificacion {self.clasificacion} dirigida por {self.director} del genero {self.genero} del año {self.año}"
    
    def convertir_json_a_funciones(self,json_data):
        for funcion_data in json_data:
             self.agregar_elemento( Funciones(
                nombre=funcion_data["nombre"],
                clasificacion=funcion_data["clasificacion"],
                director=funcion_data["director"],
                genero=funcion_data["genero"],
                año=funcion_data["año"]
            ))

    
    def mostrar_directorio(self):
        if self.check:
            dicnuf=[]
            for eleme in self.lista:
                dicnuf.append(eleme.mostrar_directorio())
                
            return dicnuf
        else:
            return {"nombre":self.nombre,"clasificacion":self.clasificacion,"director":self.director,"genero":self.genero,"año":self.año}


if __name__ == "__main__":
    print("Hola mundo")

    func = Funciones()
    dos = Funciones("2das2", "das", "das", "das", "das")
    tres = Funciones("3das3", "das", "das", "das", "das")
    sos = Funciones("4das4", "das", "das", "das", "das")
    func.agregar_elemento(dos)
    func.agregar_elemento(sos)
    print(func.mostrar_directorio())
    print(func.leer_lista())
    print(func.leer_elemento(sos))
    print(func)
    lop =Funciones()
    json_data=func.read("funciones.json")
    lop.convertir_json_a_funciones(json_data)
    print(lop.mostrar_directorio())
   
   # func.safe("funciones.json",str(func.mostrar_directorio()))
