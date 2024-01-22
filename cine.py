from salas import Salas,Funciones
from listas import Listas
class Cine(Listas):
    def __init__(self, nombre =None, direccion=None,gerente =None,snack = None, salas=None):
        if nombre == None:
             super().__init__(True)
        else:
             super().__init__(False)
        self.nombre = nombre
        self.direccion = direccion
        self.gerente = gerente
        self.snack = snack #deve de ser numero de snacks que hay 
        self.salas = salas
        
    def __str__(self):
        if self.lista:
            return str(self.elementos)+ " son el numero de cines que hay en la lista"
        return f"El cine {self.nombre} en la direcion {self.direccion} por el gerente con {self.snack} con {self.salas}  "
        
    def convertir_json_a_cine(self,json_data):
        sala=Salas()
        uno=0
        for cine_data in json_data:
             if uno == 0:
                sala.convertir_json_a_salas(cine_data["salas"])
             self.agregar_elemento( Cine(
                nombre=cine_data["nombre"],
                direccion=cine_data["direccion"],
                gerente=cine_data["gerente"],
                snack=cine_data["snack"],
                salas=sala
            ))
        return self.mostrar_directorio()

    def mostrar_directorio(self):
        if self.check:
            dicnuf=[]
            for eleme in self.lista:
                dicnuf.append(eleme.mostrar_directorio())
            return dicnuf
        else:
            return {"nombre":self.nombre,"direccion":self.direccion,"gerente":self.gerente,"snack":self.snack,"salas":self.salas.mostrar_directorio()}

if __name__ == "__main__":
    print("Hola mundo")
    lop = Cine()

    func=Funciones()
    dos=Funciones("2das2","das","das","das","das")
    tres=Funciones("3das3","das","das","das","das")
    func.agregar_elemento(dos)
    func.agregar_elemento(tres)
    salas=Salas()
    sala1=Salas(1, 100, 10, "Juan", func) 
    sala2=Salas(2, 100, 10, "Juan",func)
    salas.agregar_elemento(sala1)
    salas.agregar_elemento(sala2)
    cine2 = Cine("Citicinamas", "Av. 2", "Perez", 1,salas )
    cine = Cine("Cinepolis", "Av. 1", "Juan", 1, salas)
    lop.agregar_elemento(cine)
   # print(lop.leer_lista())
   # print(lop)
   # print(lop.mostrar_directorio())
    fomo= Cine()
    json_data = lop.read("cine.json")
    fomo.convertir_json_a_cine(json_data)
    print(fomo.mostrar_directorio())
   # lop.safe("cine.json",str(lop.mostrar_directorio()))
    
