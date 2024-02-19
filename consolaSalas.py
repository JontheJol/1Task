from salas import Salas,Funciones
from consolaFunciones import menuFunciones

class menuSalas:
    def __init__(self, salas=None):
        self.menuFunciones = None
        self.salas = Salas()
        if salas == None:
            self.safejson = True
            salas = Salas()
            json_data = salas.read("salas.json")
            salas.convertir_json_a_salas(json_data)
            self.salas = salas
        else:
            self.safejson = False
            self.salas.agregar_elemento(salas)
    def menu(self):
        print("Bienvenido a trabajar con salas")

        print("1. Crear una sala\n2. Ver la sala\n3. Modificar un aspecto de la sala\n4. Eliminar una sala")
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
            print("1. Crear una sala\n2. Ver la sala\n3. Modificar un aspecto de la sala\n4. Eliminar una sala")
            print("5. Salir")
            opcion = int(input("Ingrese la opción que desea realizar: "))
            if self.safejson:
                self.guardar()
        if not self.safejson:
            return self.salas

    
    def agregar(self):
        print("Ingrese los datos de la sala")
        numero = input("Ingrese el número de la sala: ")
        can_sillas = input("Ingrese la cantidad de sillas de la sala: ")
        altura = input("Ingrese la altura de la sala: ")
        encargado = input("Ingrese el nombre del encargado de la sala: ")
        self.menuFunciones = menuFunciones(Funciones())
        funciones = self.menuFunciones.menu()
        self.salas.agregar_elemento(Salas(numero, can_sillas, altura, encargado, funciones))
        self.mostrar()


    def mostrar(self):
        print("las salas que hay son: ")
        print(self.salas.mostrar_directorio())
        input("Presione enter para continuar")
    def modificar(self):
        self.mostrar()
        check = False
        while check == False:
            print("Ingrese el id del sala que desea modificar")
            ids = int(input("Ingrese el id del cine: "))
            if ids <= len(self.salas.lista):
                check = True
            else:
                print("ingrese valor correcto")
        print("Ingrese los datos de la sala")
        numero = input("Ingrese el número de la sala: ")
        can_sillas = input("Ingrese la cantidad de sillas de la sala: ")
        altura = input("Ingrese la altura de la sala: ")
        encargado = input("Ingrese el nombre del encargado de la sala: ")
        self.menuFunciones = menuFunciones( self.salas.lista[ids].funciones)
        funciones = self.menuFunciones.menu()

        self.salas.actualizar_elemento(ids, Salas(numero, can_sillas, altura, encargado, funciones))
        self.mostrar()

    def eliminar(self):
        ids=0
        print("se a eliminado la sala ")
        self.salas.eliminar_elemento(ids)
        self.mostrar()
    def guardar(self):
        self.salas.safe("salas.json", str(self.salas.mostrar_directorio()))

if __name__ == "__main__":
    menu = menuSalas()
    menu.menu()
    print("Gracias por usar el programa")