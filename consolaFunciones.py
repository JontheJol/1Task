from funciones import Funciones
class menuFunciones:
    def __init__(self,safejson=None,fun=None):
        self.safejson=safejson
        self.fun=Funciones()
        if self.safejson==None:
            self.safejson=True
        else:
            self.safejson=False
        

    def menu(self):
        print("bienvenido a trabajar con funciones ")
        if self.safejson == False:
            print("vas a usar las  funciones escribe  0 , usa 1 para usar  archiv json ")

            eleccion = None
            while eleccion not in [0, 1]:
                eleccion = int(input("ingrese la opcion que desea realizar(0 or 1): "))

            if eleccion != 0:
                funciones = Funciones()
                json_data = funciones.read("funciones.json")
                funciones.convertir_json_a_funciones(json_data)
                fun=funciones
        else:
            funciones = Funciones()
            json_data = funciones.read("funciones.json")
            funciones.convertir_json_a_funciones(json_data)
            self.fun=funciones
            
        print("1.crear una funcion \n2.ver la funcion\n3.modificar un aspecto de la funcion\n 4.elimiar una funcion")
        print("5.salir")

        opcion = int(input("ingrese la opcion que desea realizar: "))
        while opcion != 5:
            if opcion == 1:
               self.agregar()
            elif opcion == 2:
               self.mostrar()
            elif opcion == 3:
                self.modificar()
            elif opcion == 4:
                self.eliminar()
            else:
                print("ingrese una opcion valida")
            print("1.crear una funcion \n2.ver la funcion\n3.modificar un aspecto de la funcion\n 4.elimiar una funcion")
            print("5.salir")
            opcion = int(input("ingrese la opcion que desea realizar: "))
        if self.safejson == True:
            self.guardar()
#TODO: agregar la funcion de agregar, mostrar, modificar y eliminar
    def agregar(self):
         print("ingrese los datos de la funcion")
         nombre= input("ingrese el nombre de la funcion: ")
         clasificacion = input("ingrese la clasificacion de la funcion: ")
         director = input("ingrese el nombre del director: ")
         genero = input("ingrese el genero de la funcion: ")
         año = input("ingrese el año de la funcion: ")
         self.fun.agregar_elemento(Funciones(nombre,clasificacion,director,genero,año))
         self.mostrar()
         # print(fun.mostrar_directorio())
    def mostrar(self):
         print("las funciones que hay son: ")
         print(self.fun.mostrar_directorio())
         input("presione enter para continuar")
    
    def modificar(self):
         print("elige la funcion que desea modificar")
         self.mostrar()
         elecion= int(input("ingrese el numero  de la funcion que desea modificar: "))
         print("ingrese los datos de la funcion")
         nombre= input("ingrese el nombre de la funcion: ")
         clasificacion = input("ingrese la clasificacion de la funcion: ")
         director = input("ingrese el nombre del director: ")
         genero = input("ingrese el genero de la funcion: ")
         año = input("ingrese el año de la funcion: ")
         #posiblemente da error en la siguiente linea
         self.fun.actualizar_elemento(elecion,Funciones(nombre,clasificacion,director,genero,año))
        # print(fun.mostrar_directorio())
    def eliminar(self):
        print("elige la funcion que desea eliminar")
        self.mostrar()
        elecion= int(input("ingrese el numero  de la funcion que desea eliminar: "))
        self.fun.eliminar_elemento(elecion)
        # print(fun.mostrar_directorio())
    def guardar(self):
        self.fun.safe("funciones.json",str(self.fun.mostrar_directorio()))
        print("se guardo correctamente")
if __name__ == "__main__":
    menu=menuFunciones()
    menu.menu()