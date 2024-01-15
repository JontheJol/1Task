from funciones import Funciones
import listas
class Salas:
    def __init__(self, numero, can_sillas , altura, encargado, funciones):
        self.numero = numero
        self.can_sillas = can_sillas
        self.altura = altura
        self.encargado = encargado
        self.funciones = funciones
        self.lista = listas.Listas()
        self.lista.agregar_elemento(self)
    def __str__(self):
        return f"la sala {self.numero} tiene la  cantidad de sillas {self.can_sillas} con una altua de {self.altura} dada al encargado{self.encargado},con {self.funciones}"

if __name__ == "__main__":
    print("Hola mundo")
    sala2 = Salas(2, 100, 10, "Juan", Funciones("Hanibal", "B", "forto", "Fantasia", 2001))
    sala = Salas(1, 100, 10, "Juan", Funciones("El señor de los anillos", "B", "Peter Jackson", "Fantasia", 2001))
    print(sala)
    sala.lista.agregar_elemento(sala2)
    print(sala.lista.leer_lista())
