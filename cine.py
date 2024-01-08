import salas 

class Cine:
    def __init__(self, nombre, direccion,gerente,snack, salas):
        self.nombre = nombre
        self.direccion = direccion
        self.gerente = gerente
        self.snack = snack
        self.salas = salas

if __name__ == "__main__":
    print("Hola mundo")
    cine = Cine("Cinepolis", "Av. 1", "Juan", "Palomitas", salas.Salas(1, 100, 10, "Juan", salas.Funciones("El señor de los anillos", "B", "Peter Jackson", "Fantasia", 2001)))
    print(cine.salas.funciones.nomebre)
