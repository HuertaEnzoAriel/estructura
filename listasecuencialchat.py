import numpy as np

class ListaSecuencial:
    def __init__(self, maximo):
        self.__maximo = maximo
        self.__cant = 0
        self.__arreglo = np.empty(maximo, dtype=int)

    def vacia(self):
        return self.__cant == 0

    def llena(self):
        return self.__cant == self.__maximo

    def insertarPorposicion(self, pos, elem):
        if self.llena():
            raise Exception("La lista está llena")
        if pos < 0 or pos > self.__cant:
            raise Exception("Posición inválida")
        # Desplazar a la derecha desde la última posición hasta pos
        for i in range(self.__cant, pos, -1):
            self.__arreglo[i] = self.__arreglo[i - 1]
        self.__arreglo[pos] = elem
        self.__cant += 1

    def insertarPorContenido(self, elem):
        if self.llena():
            raise Exception("La lista está llena")

        pos = 0
        # buscar la posición correcta
        while pos < self.__cant and self.__arreglo[pos] < elem:
            pos += 1

        # desplazar a la derecha
        for i in range(self.__cant, pos, -1):
            self.__arreglo[i] = self.__arreglo[i - 1]

        self.__arreglo[pos] = elem
        self.__cant += 1


    def suprimir(self, pos):
        if self.vacia():
            raise Exception("La lista está vacía")
        if pos < 0 or pos >= self.__cant:
            raise Exception("Posición inválida")
        eliminado = self.__arreglo[pos]
        # Desplazar a la izquierda desde pos
        for i in range(pos, self.__cant - 1):
            self.__arreglo[i] = self.__arreglo[i + 1]
        self.__cant -= 1
        return eliminado

    def recuperar(self, pos):
        if pos < 0 or pos >= self.__cant:
            raise Exception("Posición inválida")
        return self.__arreglo[pos]

    def recorrer(self):
        return [int (self.__arreglo[i]) for i in range(self.__cant)]

if __name__=='__main__':
    l=ListaSecuencial(4)
    l.insertarPorContenido(10)
    l.insertarPorContenido(90)
    l.insertarPorContenido(50)
    l.insertarPorContenido(30)
    # print(f"elemento borrado: {l.suprimir(2)}")
    print(l.recorrer())
    
