from cine import Cine
from consolaSalas import menuSalas

class menuCines:
    def __init__(self,safejson = None,cines = None): 
        self.menuSalas = None
        if safejson == None:
            self.safejson = True
            self.cines = Cine()
        else:
            self.safejson = False
            if cines == None:
                self.cines = Cine()
            else:
                self.cines = cines


    def menu(self):
        print("Bienvenido a trabajar con cines")
        #cargar  JSON o no
        if self.safejson == False:
            print("Vas a usar los cines? Escribe 0, usa 1 para usar un archivo JSON")
            eleccion = None
            while eleccion not in [0, 1]:
                eleccion = int(input("Ingrese la opción que desea realizar (0 or 1): "))
            if eleccion != 0:
                cines = Cine()
                json_data = cines.read("cine.json")
                cines.convertir_json_a_cines(json_data)
                self.cines = cines
        else:
            cines = Cine()
            json_data = cines.read("cine.json")
            cines.convertir_json_a_cine(json_data)
            self.cines = cines
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
        if self.safejson == True:
            self.guardar()
    def agregar(self):
        print("Ingrese los datos del cine")
        nombre = input("Ingrese el nombre del cine: ")
        direccion = input("Ingrese la dirección del cine: ")
        telefono = input("Ingrese el teléfono del cine: ")
        self.menuSalas = menuSalas(self.safejson, self.cines.salas)
        salas = self.menuSalas.menu()
        self.cines.agregar_elemento(Cine(nombre, direccion, telefono, salas))
        self.mostrar()
    def mostrar(self):
        print("las cines que hay son: ")
        print(self.cines.mostrar_directorio())
        input("Presione enter para continuar")
    def modificar(self):
        check = False
        while check == False:
            print("Ingrese el id del cine que desea modificar")
            ids = int(input("Ingrese el id del cine: "))
            if self.cines.leer_elemento(ids) != None:
                check = True
            else:
                print("Ingrese un id valido")
        print("Ingrese los nuevos datos del cine")
        nombre = input("Ingrese el nombre del cine: ")
        direccion = input("Ingrese la dirección del cine: ")
        gerente = input("Ingrese el nombre del gerente: ")
        snack = input("Ingrese la cantidad de snacks: ")
        self.menuSalas = menuSalas(self.safejson, self.cines.salas)
        salas = self.menuSalas.menu()
        self.cines.actualizar_elemento(ids, Cine(nombre, direccion, telefono, salas))
        self.mostrar()
    def eliminar(self):
        check = False
        while check == False:
            print("Ingrese el id del cine que desea eliminar")
            ids = int(input("Ingrese el id del cine: "))
            if self.cines.leer_elemento(ids) != None:
                check = True
            else:
                print("Ingrese un id valido")
        self.cines.eliminar_elemento(ids)
        self.mostrar()
    def guardar(self):
        self.cines.save("cine.json")
        print("Se guardaron los cines en cines.json")

if __name__ == "__main__":
    menu = menuCines()
    menu.menu()
    print("Adios")