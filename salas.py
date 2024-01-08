# Purpose: Clase que representa una sala de cine
import funciones 
from funciones import Funciones
class Salas:
    def __init__(self, numero, can_sillas , altura, encargado, funciones):
        self.numero = numero
        self.can_sillas = can_sillas
        self.altura = altura
        self.encargado = encargado
        self.funciones = funciones

if __name__ == "__main__":
    print("Hola mundo")
    sala = Salas(1, 100, 10, "Juan", Funciones("El señor de los anillos", "B", "Peter Jackson", "Fantasia", 2001))
    print(sala.funciones.nomebre)