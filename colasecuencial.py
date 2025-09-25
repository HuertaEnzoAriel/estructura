import numpy as np
class colasecuencial:
    __pri:int
    __ult:int
    __arreglo:np
    __cant:int
    __tamano:int
    
    def __init__(self, dimension):
        self.__pri=-1
        self.__ult=-1
        self.__arreglo=np.empty(dimension,dtype=int)
        self.__tamano=dimension
        self.__cant=0
    
    def vacia(self):
        return self.__cant==0
    def llena(self):
        return self.__cant==self.__tamano
    def getcant(self):
        return self.__cant
    def insertar(self, elem):
        if not self.llena():
            if self.vacia():
                self.__pri=(self.__pri+1)%self.__tamano
                self.__ult=(self.__ult+1)%self.__tamano
                self.__arreglo[self.__ult]=elem
            else:
                self.__ult=(self.__ult+1)%self.__tamano
                self.__arreglo[self.__ult]=elem
            self.__cant+=1
        else:
            return print("la cola esta llena")
    def suprimir(self):
        if self.vacia():
            return print("la cola esta vacia")
        else:
            borrado=self.__arreglo[self.__pri]
            self.__pri=(self.__pri+1)%self.__tamano
            self.__cant-=1
            return borrado
if __name__ == '__main__':
    cs=colasecuencial(5)
    cs.insertar(5)
    cs.insertar(4)
    cs.insertar(3)
    cs.insertar(2)
    cs.insertar(1)
    while cs.getcant():
        print(cs.suprimir())
