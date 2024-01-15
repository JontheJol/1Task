import salas 
import listas

class Cine:
    def __init__(self, nombre, direccion,gerente,snack, salas):
        self.nombre = nombre
        self.direccion = direccion
        self.gerente = gerente
        self.snack = snack #deve de ser numero de snacks que hay 
        self.salas = salas
        self.lista = listas.Listas()
        self.lista.agregar_elemento(self)
        
    def __str__(self):
        return f"El cine {self.nombre} en la direcion {self.direccion} por el gerente con {self.snack} con {self.salas}  "
        

if __name__ == "__main__":
    print("Hola mundo")
    cine2 = Cine("Citicinamas", "Av. 2", "Perez", 1, salas.Salas(2, 100, 10, "Juan", salas.Funciones("Hanibal", "B", "forto", "Fantasia", 2001)))
    cine = Cine("Cinepolis", "Av. 1", "Juan", 1, salas.Salas(1, 100, 10, "Juan", salas.Funciones("El señor de los anillos", "B", "Peter Jackson", "Fantasia", 2001)))
    print(cine)
    cine.lista.agregar_elemento(cine2)
    print(cine.lista.leer_lista())
    
