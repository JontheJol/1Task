import funciones 
from funciones import Funciones
class Salas:
    def __init__(self, numero, can_sillas , altura, encargado, funciones):
        self.numero = numero
        self.can_sillas = can_sillas
        self.altura = altura
        self.encargado = encargado
        self.funciones = funciones
    def __str__(self):
        return f"la sala {self.numero} tiene la  cantidad de sillas {self.can_sillas} con una altua de {self.altura} dada al encargado{self.encargado},con {self.funciones}"

if __name__ == "__main__":
    print("Hola mundo")
    sala = Salas(1, 100, 10, "Juan", Funciones("El señor de los anillos", "B", "Peter Jackson", "Fantasia", 2001))
    print(sala)