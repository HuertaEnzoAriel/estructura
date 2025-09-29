class Nodo:
    def __init__(self, clave):
        self.__clave = clave        # atributo privado
        self.__izq = None           # subárbol izquierdo
        self.__der = None           # subárbol derecho

    # Métodos públicos para acceder a los atributos
    def get_clave(self):
        return self.__clave

    def get_izq(self):
        return self.__izq

    def get_der(self):
        return self.__der

    def set_izq(self, nodo):
        self.__izq = nodo

    def set_der(self, nodo):
        self.__der = nodo


class ArbolBinarioBusqueda:
    def __init__(self):
        self.__raiz = None      # atributo privado

    # ---------------- MÉTODOS PÚBLICOS ----------------

    def crear(self):
        """Inicializa el árbol vacío"""
        self.__raiz = None

    def insertar(self, clave):
        """Inserta una clave manteniendo la propiedad del ABB"""
        self.__raiz = self.__insertar(self.__raiz, clave)

    def buscar(self, clave):
        """Busca una clave en el árbol"""
        nodo = self.__buscar(self.__raiz, clave)
        if nodo:
            print(f"Elemento {clave} encontrado")
        else:
            print("Elemento inexistente")

    def suprimir(self, clave):
        """Elimina una clave del árbol"""
        self.__raiz = self.__suprimir(self.__raiz, clave)

    def inorden(self):
        """Recorrido en inorden (izq, raíz, der)"""
        print("Recorrido Inorden:")
        self.__inorden(self.__raiz)
        print()

    def preorden(self):
        """Recorrido en preorden (raíz, izq, der)"""
        print("Recorrido Preorden:")
        self.__preorden(self.__raiz)
        print()

    def postorden(self):
        """Recorrido en postorden (izq, der, raíz)"""
        print("Recorrido Postorden:")
        self.__postorden(self.__raiz)
        print()

    def altura(self):
        """Devuelve la altura del árbol"""
        return self.__altura(self.__raiz)

    # ---------------- MÉTODOS PRIVADOS ----------------

    def __insertar(self, nodo, clave):
        if nodo is None:
            return Nodo(clave)
        if clave < nodo.get_clave():
            nodo.set_izq(self.__insertar(nodo.get_izq(), clave))
        elif clave > nodo.get_clave():
            nodo.set_der(self.__insertar(nodo.get_der(), clave))
        else:
            print("Error: elemento ya existente.")
        return nodo

    def __buscar(self, nodo, clave):
        if nodo is None:
            return None
        if clave == nodo.get_clave():
            return nodo
        elif clave < nodo.get_clave():
            return self.__buscar(nodo.get_izq(), clave)
        else:
            return self.__buscar(nodo.get_der(), clave)

    def __minimo(self, nodo):
        while nodo.get_izq() is not None:
            nodo = nodo.get_izq()
        return nodo

    def __suprimir(self, nodo, clave):
        if nodo is None:
            return nodo

        if clave < nodo.get_clave():
            nodo.set_izq(self.__suprimir(nodo.get_izq(), clave))
        elif clave > nodo.get_clave():
            nodo.set_der(self.__suprimir(nodo.get_der(), clave))
        else:
            # Caso 1: sin hijos
            if nodo.get_izq() is None and nodo.get_der() is None:
                return None
            # Caso 2: un hijo
            elif nodo.get_izq() is None:
                return nodo.get_der()
            elif nodo.get_der() is None:
                return nodo.get_izq()
            # Caso 3: dos hijos
            sucesor = self.__minimo(nodo.get_der())
            nodo._Nodo__clave = sucesor.get_clave()
            nodo.set_der(self.__suprimir(nodo.get_der(), sucesor.get_clave()))
        return nodo

    def __inorden(self, nodo):
        if nodo:
            self.__inorden(nodo.get_izq())
            print(nodo.get_clave(), end=" ")
            self.__inorden(nodo.get_der())

    def __preorden(self, nodo):
        if nodo:
            print(nodo.get_clave(), end=" ")
            self.__preorden(nodo.get_izq())
            self.__preorden(nodo.get_der())

    def __postorden(self, nodo):
        if nodo:
            self.__postorden(nodo.get_izq())
            self.__postorden(nodo.get_der())
            print(nodo.get_clave(), end=" ")

    def __altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self.__altura(nodo.get_izq()), self.__altura(nodo.get_der()))
