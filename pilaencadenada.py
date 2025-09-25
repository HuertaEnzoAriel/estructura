import numpy as np
class pilasecuencial:
    __tope:int
    __cantidad:int
    __arreglo:np
    __tamano:int
    def __init__(self,dimension):
        self.__tope=-1
        self.__cantidad=0
        self.__arreglo=np.empty(dimension,dtype=int)
        self.__tamano=dimension
    def gettop(self):
        return self.__tope
    def getcant(self):
        return self.__cantidad
    def vacia(self):
        return self.__cantidad==0
    def llena(self):
        return self.__cantidad==self.__tamano
    def insertar(self, item):
        if not self.llena():
            self.__tope+=1
            self.__arreglo[self.__tope]=item
            self.__cantidad+=1
        else:
            return print("pila llena")
    def suprimir(self):
        if not self.vacia():
            borrado=self.__arreglo[self.__tope]
            self.__tope-=1
            self.__cantidad-=1
            return borrado


if __name__ == '__main__':
    # pilaS = pilasecuencial(4)
    # print("Pila Secuencial")
    # pilaS.insertar(1)
    # pilaS.insertar(2)
    # pilaS.insertar(3)
    # pilaS.insertar(4)
    # pilaS.insertar(5)
    # while pilaS.vacia() != True:
    #     print(pilaS.suprimir())
    dimension=int(input("ingresa la dimension de la pila: "))
    p=pilasecuencial(dimension)
    decimal=int(input("ingresa el numero a convertir: "))
    aux=decimal
    while aux>=1:
        modulo=aux%2
        aux=aux//2
        p.insertar(modulo)
    
    print(f"el numero en binario es:")
    i=0
    lista=np.zeros(dimension,dtype=int)
    while not p.vacia():
        lista[i]=p.suprimir()
        i+=1
    print(lista[:i])
