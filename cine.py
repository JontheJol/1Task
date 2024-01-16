import salas 
from listas import Listas
class Cine(Listas):
    def __init__(self, nombre =None, direccion=None,gerente =None,snack = None, salas=None):
        super().__init__()
        self.nombre = nombre
        self.direccion = direccion
        self.gerente = gerente
        self.snack = snack #deve de ser numero de snacks que hay 
        self.salas = salas
        self.lista = []
        
    def __str__(self):
        if self.lista:
            return str(self.elementos)+ " son el numero de cines que hay en la lista"
        return f"El cine {self.nombre} en la direcion {self.direccion} por el gerente con {self.snack} con {self.salas}  "
        

if __name__ == "__main__":
    print("Hola mundo")
    lop = Cine()
    cine2 = Cine("Citicinamas", "Av. 2", "Perez", 1, salas.Salas(2, 100, 10, "Juan", salas.Funciones("Hanibal", "B", "forto", "Fantasia", 2001)))
    cine = Cine("Cinepolis", "Av. 1", "Juan", 1, salas.Salas(1, 100, 10, "Juan", salas.Funciones("El señor de los anillos", "B", "Peter Jackson", "Fantasia", 2001)))
    lop.agregar_elemento(cine)
    print(lop.leer_lista())
    print(lop)
    
