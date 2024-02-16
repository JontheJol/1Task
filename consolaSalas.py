from salas import Salas,Funciones
from consolaFunciones import menuFunciones

class menuSalas:
    def __init__(self, salas=None):
        self.menuFunciones = None
        if salas == None:
            self.safejson = True
            self.salas = Salas()
            salas = Salas()
            json_data = salas.read("salas.json")
            salas.convertir_json_a_salas(json_data)
            self.salas = salas
        else:
            self.safejson = False
            self.salas = salas    
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
        if self.safejson:
            self.guardar()
        else:
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

        print("Ingrese los datos de la sala")
        numero = input("Ingrese el número de la sala: ")
        can_sillas = input("Ingrese la cantidad de sillas de la sala: ")
        altura = input("Ingrese la altura de la sala: ")
        encargado = input("Ingrese el nombre del encargado de la sala: ")
        self.menuFunciones = menuFunciones( self.salas.lista[0].funciones)
        funciones = self.menuFunciones.menu()
        self.salas.actualizar_elemento(0, Salas(numero, can_sillas, altura, encargado, funciones))
        self.mostrar()

    def eliminar(self):
        numero = 0 
        print("se a eliminado la sala ")
        self.salas.eliminar_elemento(numero)
        self.mostrar()
    def guardar(self):
        self.salas.safe("salas.json", str(self.salas.mostrar_directorio()))

if __name__ == "__main__":
    menu = menuSalas()
    menu.menu()
    print("Gracias por usar el programa")