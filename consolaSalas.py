from salas import Salas
from consolaFunciones import menuFunciones

class menuSalas:
    def __init__(self, safejson=None, salas=None):
        self.salas = Salas()
        self.menuFunciones = None
        if safejson == None:
            self.safejson = True
        else:
            self.safejson = False
    def menu(self):
        print("Bienvenido a trabajar con salas")
        if self.safejson == False:
            print("Vas a usar las salas? Escribe 0, usa 1 para usar un archivo JSON")
            eleccion = None
            while eleccion not in [0, 1]:
                eleccion = int(input("Ingrese la opción que desea realizar (0 or 1): "))
            if eleccion != 0:
                salas = Salas()
                json_data = salas.read("salas.json")
                salas.convertir_json_a_salas(json_data)
                self.salas = salas
        else:
            salas = Salas()
            json_data = salas.read("salas.json")
            salas.convertir_json_a_salas(json_data)
            self.salas = salas
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
        if self.safejson == True:
            self.guardar()
    def agregar(self):
        print("Ingrese los datos de la sala")
        numero = input("Ingrese el número de la sala: ")
        can_sillas = input("Ingrese la cantidad de sillas de la sala: ")
        altura = input("Ingrese la altura de la sala: ")
        encargado = input("Ingrese el nombre del encargado de la sala: ")
        self.menuFunciones = menuFunciones(self.safejson, self.salas.funciones)
        funciones = self.menuFunciones.menu()
        self.salas.agregar_elemento(Salas(numero, can_sillas, altura, encargado, funciones))
        self.mostrar()

    def mostrar(self):
        print("las salas que hay son: ")
        print(self.salas.mostrar_directorio())
        input("Presione enter para continuar")
    def modificar(self):
        check = False
        while check == False:
            print("Ingrese el número de la sala que desea modificar")
            numero = input("Ingrese el número de la sala: ")
            if numero <= self.salas.elementos and numero >= self.salas.elementos:
                check = True

        print("Ingrese los datos de la sala")
        numero = input("Ingrese el número de la sala: ")
        can_sillas = input("Ingrese la cantidad de sillas de la sala: ")
        altura = input("Ingrese la altura de la sala: ")
        encargado = input("Ingrese el nombre del encargado de la sala: ")
        self.menuFunciones = menuFunciones(self.safejson, self.salas.funciones)
        funciones = self.menuFunciones.menu()
        self.salas.actualizar_elemento(numero, Salas(numero, can_sillas, altura, encargado, funciones))
        self.mostrar()
    def eliminar(self):
        print("Ingrese el número de la sala que desea eliminar")
        numero = input("Ingrese el número de la sala: ")
        self.salas.eliminar_elemento(numero)
        self.mostrar()
    def guardar(self):
        self.salas.safe("salas.json", str(self.salas.mostrar_directorio()))

if __name__ == "__main__":
    menu = menuSalas()
    menu.menu()
    print("Gracias por usar el programa")