from random import random
class nodo:
    __nodo:int
    __sig:None
    def __init__(self,item):
        self.__nodo=item
        self.__sig=None
    def setsig(self, sig):
        self.__sig=sig
    def getelem(self):
        return self.__nodo
    def getsig(self):
        return self.__sig
    
class Cola:
    __ult:nodo
    __pri:nodo
    __cant:int
    def __init__(self):
        self.__ult=None
        self.__pri=None
        self.__cant=0
    def vacia(self):
        return self.__cant==0
    def insertar(self,item):
        nuevo=nodo(item)
        if self.vacia():
            self.__pri=nuevo
        else:
            self.__ult.setsig(nuevo)
        self.__ult=nuevo
        self.__cant+=1
    def getult(self):
        return self.__ult.getelem()
    def getcant(self):
        return self.__cant
    def getpri(self):
        return self.__pri.getelem()
    def suprimir(self):
        if self.vacia():
            return print("cola vacia")
        else:
            borrado=self.__pri.getelem()
            self.__cant-=1
            self.__pri=self.__pri.getsig()
            return borrado

if __name__=='__main__':
    cola=Cola()
    frecuenciallegada=10
    empleado=0
    promedioatencion=15
    tms=300
    reloj=0
    cantidadAtendido=0
    maxespera=0
    cantllegados=0
    while reloj < tms:
        if random() <= 1/frecuenciallegada:
        # if reloj % frecuenciallegada==0:
            cola.insertar(reloj)
            # print(f"cliente: {cola.getpri()} llega a los:{reloj} min")
            cantllegados+=1

        if empleado==0 and not cola.vacia():
            # print(f"cliente: {cola.getpri()} atendido a los:{reloj} min")
            llegada=cola.suprimir()
            espera=reloj-llegada
            if espera>maxespera:
                maxespera=espera
            empleado=promedioatencion
            cantidadAtendido+=1
        if empleado > 0:
            empleado-=1
        reloj+=1
    if cola.vacia():
        print(f"Todos los solicitantes fueron atendidos")
    else:
        print(f"Clientes atendidos: {cantllegados-cola.getcant()}")
        # while cola.suprimir():
        #     i+=1
        print(f"Tiempo maximo de espera: {maxespera} minutos y {cola.getcant()} clientes sin atender")
        print(f"Clientes en total {cantllegados}")
