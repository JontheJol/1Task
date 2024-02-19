from converJ import Archivo
class Listas(Archivo):
    def __init__(self,check):
        super().__init__
        self.lista = []
        self.elementos = 0
        self.dic={}
        self.check= check
      #  self.dicnuf=[]
 

    def __str__(self):
        return str(self.lista)

    def mostrar_directorio(self):
        pass

    def agregar_elemento(self, elemento):
        self.lista.append(elemento)
        self.elementos += 1
  
    def eliminar_elemento(self, index):
        if 0 <= index < len(self.lista):
            self.lista.pop(index)
            self.elementos -= 1
        else:
            raise ValueError("El índice está fuera del rango de la lista")

    def actualizar_elemento(self, ids, func):
        if 0 <= int(ids) <= len(self.lista):
            if ids==0:
                self.lista.insert(0, func)
            else:
                self.lista.pop(ids)
                self.lista.insert(ids, func)
        else:
            raise ValueError("El elemento no se encuentra en la lista")

    def leer_lista(self):
        lista_str = ""
        for elemento in self.lista:
            lista_str += f"{elemento}\n"
        return lista_str

    def leer_elemento(self, elemento):
        if elemento in self.lista:
            return self.lista[self.lista.index(elemento)]
        else:
            raise ValueError("El elemento no se encuentra en la lista")
