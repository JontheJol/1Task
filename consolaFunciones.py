import funciones
class menuFunciones:
    def menu(self):
        print("bienvenido a trabajar con funciones ")
        print("1.crear una funcion \n2.ver la funcion\n3.modificar un aspecto de la funcion\n 4.elimiar una funcion")
        print("5.salir")
        opcion = int(input("ingrese la opcion que desea realizar: "))
        while opcion != 5:
            if opcion == 1:
                fun = Funciones()
                print("ingrese los datos de la funcion")
                nombre= input("ingrese el nombre de la funcion: ")
                clasificacion = input("ingrese la clasificacion de la funcion: ")
                director = input("ingrese el nombre del director: ")
                genero = input("ingrese el genero de la funcion: ")
                año = input("ingrese el año de la funcion: ")
                fun.agregar_elemento(Funciones(nombre,clasificacion,director,genero,año))
            elif opcion == 2:
                print("las funciones que hay son: ")
                funciones.mostrar_directorio()
            elif opcion == 3:
                print("elige la funcion que desea modificar")
                print(funciones.mostrar_directorio())

                funciones.modificar_funcion()
            elif opcion == 4:
                funciones.eliminar_funcion()
            else:
                print("ingrese una opcion valida")
            print("1.crear una funcion \n2.ver la funcion\n3.modificar un aspecto de la funcion\n 4.elimiar una funcion")
            print("5.salir")
            opcion = int(input("ingrese la opcion que desea realizar: "))