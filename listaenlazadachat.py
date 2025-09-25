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
    __cabeza:Nodo
    __cant:int
    def __init__(self):
        self.__cabeza = None
        self.__cant = 0

    def vacia(self):
        return self.__cant==0

    def insertarporposicion(self, pos, elem):
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

    def insertarporcontenido(self,elem):
        nuevo=Nodo(elem)
        if self.vacia() or self.__cabeza.getElem() >= elem:
            nuevo.setsig(self.__cabeza)
            self.__cabeza=nuevo
        else:
            anterior=self.__cabeza
            actual=anterior.getsig()
            while actual is not None and actual.getElem() < elem:
                anterior=actual
                actual=actual.getsig()
            nuevo.setsig(actual)
            anterior.setsig(nuevo)
        self.__cant+=1
         

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
if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.insertarporcontenido(50)
    lista.insertarporcontenido(20)
    lista.insertarporcontenido(40)
    lista.insertarporcontenido(10)
    lista.insertarporcontenido(30)
    print(lista.recorrer())  # 👉 [10, 20, 30, 40, 50]

