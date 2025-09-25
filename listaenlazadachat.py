class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__sig = None

    def getElem(self):
        return self.__dato

    def getsig(self):
        return self.__sig

    def setsig(self, sig):
        self.__sig = sig


class ListaEnlazada:
    def __init__(self):
        self.__cabeza = None
        self.__cant = 0

    def vacia(self):
        return self.__cabeza is None

    def insertar(self, pos, elem):
        if pos < 0 or pos > self.__cant:
            raise Exception("Posición inválida")
        nuevo = Nodo(elem)
        if pos == 0:  # Inserta al inicio
            nuevo.setsig(self.__cabeza)
            self.__cabeza = nuevo
        else:
            anterior = self.__cabeza
            for _ in range(pos - 1):
                anterior = anterior.getsig()
            nuevo.setsig(anterior.getsig())
            anterior.setsig(nuevo)
        self.__cant += 1

    def suprimir(self, pos):
        if self.vacia():
            raise Exception("La lista está vacía")
        if pos < 0 or pos >= self.__cant:
            raise Exception("Posición inválida")
        if pos == 0:
            eliminado = self.__cabeza.getElem()
            self.__cabeza = self.__cabeza.getsig()
        else:
            anterior = self.__cabeza
            for _ in range(pos - 1):
                anterior = anterior.getsig()
            eliminado = anterior.getsig().getElem()
            anterior.setsig(anterior.getsig().getsig())
        self.__cant -= 1
        return eliminado

    def recuperar(self, pos):
        if pos < 0 or pos >= self.__cant:
            raise Exception("Posición inválida")
        aux = self.__cabeza
        for _ in range(pos):
            aux = aux.getsig()
        return aux.getElem()

    def recorrer(self):
        elementos = []
        aux = self.__cabeza
        while aux is not None:
            elementos.append(aux.getElem())
            aux = aux.getsig()
        return elementos
