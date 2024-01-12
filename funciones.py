class Funciones:
    def __init__(self, nomebre, clasificacion, director, genero, año):
        self.nomebre = nomebre
        self.clasificacion = clasificacion
        self.director = director
        self.genero = genero
        self.año = año
        self.funciones = []
        self.check=0
    def __str__(self):
        if self.check == 1:
            f=self.funciones
        else:
            f ={"nombre":self.nomebre,
            "clasificacion": self.clasificacion,
            "Director":self.director,
            "genero":self.genero,
            "año": self.año}
        return str(f)
        #añade funcion
    def add_funciones(self,funcion):
        if self.check == 0 :
            self.funciones=[{"nombre":self.nomebre,
            "clasificacion": self.clasificacion,
            "Director":self.director,
            "genero":self.genero,
            "año": self.año}]
            self.funciones.append(funcion)
            self.check=1
        else:
            self.funciones.append(
                {"nombre":funcion.nomebre,
                "clasificacion": funcion.clasificacion,
                "Director":funcion.director,
                "genero":funcion.genero,
                "año": funcion.año}
            )
    
    def delete_funciones(self, funcion):
        if funcion in self.funciones:
            self.funciones.remove(funcion)
        

if __name__ == "__main__":
    print("Hola mundo")
    func= Funciones("das", "das", "das", "das", "das")
    dos=Funciones("2das2", "das", "das", "das", "das")
   
    sos=Funciones("4das4", "das", "das", "das", "das")
    print(func)
    func.add_funciones(dab)
    print(func)
    func.add_funciones(dos)
    print(func)
    func.delete_funciones(dos)
    func.add_funciones(sos)
    print(func)


    
    
