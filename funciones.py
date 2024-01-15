import listas

class Funciones:
    def __init__(self, nombre, clasificacion, director, genero, año):
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.director = director
        self.genero = genero
        self.año = año
        self.lista = listas.Listas()
       

    def __str__(self):
        f = {"nombre": self.nombre,
                "clasificacion": self.clasificacion,
                "director": self.director,
                "genero": self.genero,
                "año": self.año}
        return str(f)


if __name__ == "__main__":
    print("Hola mundo")
    func = Funciones("das", "das", "das", "das", "das")
    dos = Funciones("2das2", "das", "das", "das", "das")
    sos = Funciones("4das4", "das", "das", "das", "das")
    print(func)
    func.lista.agregar_elemento(dos)
    print(func)
    func.lista.agregar_elemento(sos)
    print(func)
    print(func.lista.leer_lista())