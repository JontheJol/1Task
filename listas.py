class Listas:
    def __init__(self):
        self.lista = []
        self.elementos = 0
        self.dic={}
        self.dicnuf=[]
 

    def __str__(self):
        return str(self.lista)

    def mostrar_directorio(self):
        if self.lista:
            for elemento in self.lista:
                self.dicnuf.append(self.dict)
            return self.dicnuf
        else: self.dic
        return d

    def agregar_elemento(self, elemento):
        self.lista.append(elemento)
        self.elementos += 1
  
    def eliminar_elemento(self, elemento):
        if elemento in self.lista:
            self.lista.remove(elemento)
            self.elementos -= 1
        else:
            raise ValueError("El elemento no se encuentra en la lista")

    def actualizar_elemento(self, elemento_a_actualizar, nuevo_elemento):
        if elemento_a_actualizar in self.lista:
            self.lista.remove(elemento_a_actualizar)
            self.lista.append(nuevo_elemento)
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
