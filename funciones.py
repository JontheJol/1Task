class Funciones:
    def __init__(self, nomebre, clasificacion, director, genero, año):
        self.nomebre = nomebre
        self.clasificacion = clasificacion
        self.director = director
        self.genero = genero
        self.año = año
        self.funciones = []
    def __str__(self):
        return f"La funcion {self.nomebre} es de clasificacion {self.clasificacion} dirigida por {self.director} del genero {self.genero} del año {self.año}"

    def add_funciones(self,funcion):
        self.funciones.append(funcion)
        
        

if __name__ == "__main__":
    print("Hola mundo")
    func= Funciones("das", "das", "das", "das", "das")
    print(func)
    func.add_funciones= Funciones("2", "3", "4", "5", "5")
    print(func)
    
