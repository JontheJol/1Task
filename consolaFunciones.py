from funciones import Funciones
class menuFunciones:
    def menu(self):
        
        fun = Funciones()
        print("bienvenido a trabajar con funciones ")
        print("vas a usar las siguientes funciones escribe  0 o usa 1 para usar  archiv json ")

        eleccion = None
        while eleccion not in [0, 1]:
            eleccion = int(input("ingrese la opcion que desea realizar: "))

        if eleccion != 0:
            funciones = Funciones()
            json_data = funciones.read("funciones.json")
            funciones.convertir_json_a_funciones(json_data)
            fun=funciones
        
        print("1.crear una funcion \n2.ver la funcion\n3.modificar un aspecto de la funcion\n 4.elimiar una funcion")
        print("5.salir")

        opcion = int(input("ingrese la opcion que desea realizar: "))
        while opcion != 5:
            if opcion == 1:
                print("ingrese los datos de la funcion")
                nombre= input("ingrese el nombre de la funcion: ")
                clasificacion = input("ingrese la clasificacion de la funcion: ")
                director = input("ingrese el nombre del director: ")
                genero = input("ingrese el genero de la funcion: ")
                año = input("ingrese el año de la funcion: ")
                fun.agregar_elemento(Funciones(nombre,clasificacion,director,genero,año))
                # print(fun.mostrar_directorio())
            elif opcion == 2:
                print("las funciones que hay son: ")
                print(fun.mostrar_directorio())
                input("presione enter para continuar")
            elif opcion == 3:
                print("elige la funcion que desea modificar")
                print(funciones.mostrar_directorio())
                elecion= input("ingrese el numero  de la funcion que desea modificar: ")


                funciones.modificar_funcion()
            elif opcion == 4:
                funciones.eliminar_funcion()
            else:
                print("ingrese una opcion valida")
            print("1.crear una funcion \n2.ver la funcion\n3.modificar un aspecto de la funcion\n 4.elimiar una funcion")
            print("5.salir")
            opcion = int(input("ingrese la opcion que desea realizar: "))

if __name__ == "__main__":
    menu=menuFunciones()
    menu.menu()