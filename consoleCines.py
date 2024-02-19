from cine import Cine,Salas
from consolaSalas import menuSalas

class menuCines:
    def __init__(self,cines = None): 
        self.menuSalas = None
        if cines == None:
            self.safejson = True
            self.cines = Cine()
            cines = Cine()
            json_data = cines.read("cine.json")
            cines.convertir_json_a_cine(json_data)
            self.cines = cines
        else:
            self.safejson = False
            self.cines = cines


    def menu(self):
        print("Bienvenido a trabajar con cines")

        print("1. Crear un cine\n2. Ver el cine\n3. Modificar un aspecto del cine\n4. Eliminar un cine")
        print("5. Salir")

        opcion = int(input("Ingrese la opción que desea realizar: "))
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
                print("Ingrese una opción válida")
            print("1. Crear un cine\n2. Ver el cine\n3. Modificar un aspecto del cine\n4. Eliminar un cine")
            print("5. Salir")
            opcion = int(input("Ingrese la opción que desea realizar: "))
            if self.safejson:
                    self.guardar()
        if self.safejson:
            self.guardar()
        else:
            return self.cines
    def agregar(self):
        print("Ingrese los datos del cine")
        nombre = input("Ingrese el nombre del cine: ")
        direccion = input("Ingrese la dirección del cine: ")
        gerente = input("Ingrese el gerente del cine: ")
        sanack = input("Ingrese la cantidad de snacks: ")
        self.menuSalas = menuSalas(Salas())
        salas = self.menuSalas.menu()
        self.cines.agregar_elemento(Cine(nombre, direccion, gerente, sanack, salas))
        self.mostrar()

    def mostrar(self):
        print("las cines que hay son: ")
        print(self.cines.mostrar_directorio())
        input("Presione enter para continuar")
    def modificar(self):
        self.mostrar()
        check = False
        while check == False:
            print("Ingrese el id del funciones que desea modificar")
            ids = int(input("Ingrese el id del cine: "))
            if ids <= len(self.cines.lista):
                check = True
            else:
                print("ingrese valor correcto")
        print("Ingrese los nuevos datos del cine")
        nombre = input("Ingrese el nombre del cine: ")
        direccion = input("Ingrese la dirección del cine: ")
        gerente = input("Ingrese el nombre del gerente: ")
        snack = input("Ingrese la cantidad de snacks: ")
        self.menuSalas = menuSalas(self.cines.lista[ids].salas.lista[ids])
        salas = self.menuSalas.menu()
        self.cines.actualizar_elemento(ids, Cine(nombre, direccion, gerente, snack, salas))
        self.mostrar()
    def eliminar(self):
        self.mostrar()
        check = False
        while check == False:
            print("Ingrese el id del cine que desea modificar")
            ids = int(input("Ingrese el id del cine: "))
            if ids <= len(self.cines.lista):
                check = True
            else:
                print("ingrese valor correcto")
        self.cines.lista[ids].eliminar_elemento(ids)
        self.mostrar()
    def guardar(self):
        self.cines.safe("cine.json",str(self.cines.mostrar_directorio()))
        print("Se guardaron los cines en cines.json")

if __name__ == "__main__":
    menu = menuCines()
    menu.menu()
    print("Adios")