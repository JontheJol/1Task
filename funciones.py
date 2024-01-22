from listas import Listas
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
        self.dic={"nombre":self.nombre,"clasificacion":self.clasificacion,"director":self.director,"genero":self.genero,"año":self.año}


    def __str__(self):
        if self.lista:
            return str(self.elementos)+ " son el numero de funciones que hay en la lista"
        return f"La funcions {self.nombre} es de clasificacion {self.clasificacion} dirigida por {self.director} del genero {self.genero} del año {self.año}"
    
    
    def mostrar_directorio(self):
        if self.check:
            dicnuf=[]
            for eleme in self.lista:
                dicnuf.append(eleme.mostrar_directorio())
            return dicnuf
        else:
            return self.dic


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
  
    func.safe("funciones.json",str(func.mostrar_directorio()))
