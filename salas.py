from funciones import Funciones
from listas import Listas
class Salas(Listas):
    def __init__(self, numero = None, can_sillas =None , altura = None, encargado = None, funciones = None):
        if numero == None:
             super().__init__(True)
        else:
            super().__init__(False)
        self.numero = numero
        self.can_sillas = can_sillas
        self.altura = altura
        self.encargado = encargado
        self.funciones = funciones
        
    def __str__(self):
        if self.lista:
            return str(self.elementos)+ " son el numero de salas que hay en la lista"
        return f"la sala {self.numero} tiene la  cantidad de sillas {self.can_sillas} con una altua de {self.altura} dada al encargado{self.encargado},con {self.funciones}"

    def mostrar_directorio(self):
        if self.check:
            dicnuf=[]
            for eleme in self.lista:
                dicnuf.append(eleme.mostrar_directorio())
            return dicnuf
        else:
            return {"numero":self.numero,"can_sillas":self.can_sillas,"altura":self.altura,"encargado":self.encargado,"funciones":self.funciones.mostrar_directorio() or None}

if __name__ == "__main__":
    print("Hola mundo")
    func = Funciones()
    dos = Funciones("2das2", "das", "das", "das", "das")
    tres = Funciones("3das3", "das", "das", "das", "das")
    sos = Funciones("4das4", "das", "das", "das", "das")
    func.agregar_elemento(dos)
    func.agregar_elemento(sos)
    sala = Salas()
    sala2 = Salas(2, 100, 10, "Juan", func)
    sala3 = Salas(1, 100, 10, "Juan", func)
    sala.agregar_elemento(sala2)
    print(sala)
    print(sala.mostrar_directorio())
    sala.safe("salas.json",str(sala.mostrar_directorio()))
