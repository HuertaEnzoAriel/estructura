class nodo:
    __sig:None
    __elem:int

    def __init__(self,elem):
        self.__elem=elem
        self.__sig=None

    def setsig(self,sig):
        self.__sig=sig
    def getelem(self):
        return self.__elem
    def getsig(self):
        return self.__sig

class colaencadenada:
    __ult:nodo
    __pri:nodo
    __cant:int

    def __init__(self):
        self.__ult=None
        self.__pri=None
        self.__cant=0
    def vacia(self):
        return self.__cant==0
    def getcant(self):
        return self.__cant
    def insertar(self,item):
        nuevo=nodo(item)
        if self.vacia():
            self.__pri=nuevo
        else:
            self.__ult.setsig(nuevo)
        self.__ult=nuevo
        self.__cant+=1
    
    def suprimir(self):
        if self.vacia():
            return print("cola vacia")
        else:
            borrado=self.__pri.getelem()
            self.__pri=self.__pri.getsig()
            self.__cant-=1
            return borrado

if __name__=='__main__':
    ce=colaencadenada()
    ce.insertar(1)
    ce.insertar(2)
    ce.insertar(3)
    ce.insertar(4)
    while ce.getcant():
        print(ce.suprimir())
    ce.suprimir()
            
