import numpy as np


class Monticulo:
    __max:int
    __elementos:np.array
    def __init__(self, n):
        self.__max = n + 1
        self.__elementos = np.zeros(self.__max, dtype=int)
        self.__elementos[0] = 0


    def insertar(self, x):
        if self.__elementos[0] < self.__max - 1:
            self.__elementos[self.__elementos[0] + 1] = x
            self.__elementos[0] += 1
            i = self.__elementos[0]
            while i > 1 and self.__elementos[i] < self.__elementos[i // 2]:
                self.__elementos[i], self.__elementos[i // 2] = self.__elementos[i // 2], self.__elementos[i]
                i //= 2
            return True
        else:
            print("Montículo lleno.")
            return False


    def eliminar_minimo(self):
        if self.__elementos[0] > 0:
            x = self.__elementos[1]
            self.__elementos[1] = self.__elementos[int(self.__elementos[0])]
            self.__elementos[0] -= 1
            i = 1
            while (i * 2 <= self.__elementos[0]) and (
                (self.__elementos[i] > self.__elementos[i * 2]) or 
                (i * 2 + 1 <= self.__elementos[0] and self.__elementos[i] > self.__elementos[i * 2 + 1])
            ):
                if (i * 2 + 1 > self.__elementos[0]) or (self.__elementos[i * 2] < self.__elementos[i * 2 + 1]):
                    self.__elementos[i], self.__elementos[i * 2] = self.__elementos[i * 2], self.__elementos[i]
                    i = i * 2
                else:
                    self.__elementos[i], self.__elementos[i * 2 + 1] = self.__elementos[i * 2 + 1], self.__elementos[i]
                    i = i * 2 + 1
            return x
        else:
            print("Montículo vacío.")
            return None


    def mostrar(self):
        for i in range(1, int(self.__elementos[0]) + 1):
            print(f"\nNodo {self.__elementos[i]}", end="")
            if (i * 2) <= self.__elementos[0]:
                print(f" - hijo izq {self.__elementos[i * 2]}", end="")
            if (i * 2 + 1) <= self.__elementos[0]:
                print(f" - hijo der {self.__elementos[i * 2 + 1]}", end="")


if __name__ == "__main__":
    monticulo = Monticulo(10)


    # Insertar elementos
    print("Insertando elementos:")
    for num in [5, 3, 8, 1, 6]:
        monticulo.insertar(num)
        monticulo.mostrar()


    # Mostrar el estado final del montículo después de todas las inserciones
    print("\nEstado final del montículo:")
    monticulo.mostrar()


    # Eliminar el mínimo
    print("\nEliminando el mínimo:")
    while monticulo._Monticulo__elementos[0] > 0:  # Acceso a un atributo privado
        min_elem = monticulo.eliminar_minimo()
        print(f"Elemento eliminado: {min_elem}")
        monticulo.mostrar()



