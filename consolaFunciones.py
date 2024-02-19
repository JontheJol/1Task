from funciones import Funciones
class menuFunciones:
    def __init__(self,fun=None):
        self.fun=Funciones()

        if fun == None:
            self.safejson=True
            funciones = Funciones()
            json_data = funciones.read("funciones.json")
            funciones.convertir_json_a_funciones(json_data)
            self.fun=funciones
        else:
            self.safejson=False
            #verifica si el objeto esta basio
            self.fun = fun
        

    def menu(self):
        print("bienvenido a trabajar con funciones ")
            
        print("1.crear una funcion \n2.ver la funcion\n3.modificar un aspecto de la funcion\n 4.elimiar una funcion")
        print("5.salir")

        opcion = int(input("ingrese la opcion que desea realizar: "))
        while opcion != 5  and opcion != None:
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
            if self.safejson:
                    self.guardar()
        #Elecion de guardar automaticamente
        if self.safejson:
            self.guardar()
        else:
            return self.fun
#TODO: agregar la funcion de agregar, mostrar, modificar y eliminar
    def agregar(self):
         print("ingrese los datos de la funcion")
         nombre= input("ingrese el nombre de la funcion: ")
         clasificacion = input("ingrese la clasificacion de la funcion: ")
         director = input("ingrese el nombre del director: ")
         genero = input("ingrese el genero de la funcion: ")
         año = input("ingrese el año de la funcion: ")
         funciona=Funciones(nombre,clasificacion,director,genero,año)
         self.fun.agregar_elemento(funciona)
         self.mostrar()
         # print(fun.mostrar_directorio())
    def mostrar(self):
         print("las funciones que hay son: ")
         if self.fun == None:
             print("no hay funciones")
             pass
         else:
            print(self.fun.mostrar_directorio())
            input("presione enter para continuar")
        
    def modificar(self):
         self.mostrar()
         check = False
         while check == False:
             print("Ingrese el id del funciones que desea modificar")
             ids = int(input("Ingrese el id del cine: "))
             if ids <= len(self.fun.lista):
                check = True
             else:
                print("ingrese valor correcto")
         print("ingrese los datos de la funcion")
         nombre= input("ingrese el nombre de la funcion: ")
         clasificacion = input("ingrese la clasificacion de la funcion: ")
         director = input("ingrese el nombre del director: ")
         genero = input("ingrese el genero de la funcion: ")
         año = input("ingrese el año de la funcion: ")
         #posiblemente da error en la siguiente linea
         self.fun.actualizar_elemento(ids,Funciones(nombre,clasificacion,director,genero,año))
        # print(fun.mostrar_directorio())
    def eliminar(self):
        self.mostrar()
        check = False
        while check == False:
            print("Ingrese el id del cine que desea modificar")
            ids = int(input("Ingrese el id del cine: "))
            if ids <= len(self.fun.lista):
                check = True
            else:
                print("ingrese valor correcto")
        self.fun.eliminar_elemento(ids)
        # print(fun.mostrar_directorio())
    def guardar(self):
        self.fun.safe("funciones.json",str(self.fun.mostrar_directorio()))
        print("se guardo correctamente")
    def get_fun(self):
        return self.fun
    
if __name__ == "__main__":
    menu=menuFunciones()
    menu.menu()