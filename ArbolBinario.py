class Nodo:
    def __init__(self, clave):
        self.__clave = clave      # atributo privado
        self.__izq = None         # subárbol izquierdo
        self.__der = None         # subárbol derecho

    # Métodos públicos de acceso
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
        self.__raiz = None        # atributo privado

    # ---------------- MÉTODOS PÚBLICOS ----------------

    def crear(self):
        """Inicializa el árbol vacío"""
        self.__raiz = None

    def insertar(self, clave):
        """Inserta un elemento manteniendo la propiedad del ABB"""
        if self.__raiz is None:
            self.__raiz = Nodo(clave)
        else:
            self._insertar(self.__raiz, clave)

    def _insertar(self, nodo, clave):
        """Método auxiliar público para insertar"""
        if clave < nodo.get_clave():
            if nodo.get_izq() is None:
                nodo.set_izq(Nodo(clave))
            else:
                self._insertar(nodo.get_izq(), clave)
        elif clave > nodo.get_clave():
            if nodo.get_der() is None:
                nodo.set_der(Nodo(clave))
            else:
                self._insertar(nodo.get_der(), clave)
        else:
            print("Error: elemento ya existente")

    def buscar(self, clave):
        """Busca una clave en el árbol"""
        nodo = self._buscar(self.__raiz, clave)
        if nodo:
            print(f"Elemento {clave} encontrado")
        else:
            print("Elemento inexistente")

    def _buscar(self, nodo, clave):
        if nodo is None:
            return None
        if clave == nodo.get_clave():
            return nodo
        elif clave < nodo.get_clave():
            return self._buscar(nodo.get_izq(), clave)
        else:
            return self._buscar(nodo.get_der(), clave)

    def suprimir(self, clave):
        """Elimina un nodo del árbol"""
        self.__raiz = self._suprimir(self.__raiz, clave)

    def _suprimir(self, nodo, clave):
        if nodo is None:
            return nodo
        if clave < nodo.get_clave():
            nodo.set_izq(self._suprimir(nodo.get_izq(), clave))
        elif clave > nodo.get_clave():
            nodo.set_der(self._suprimir(nodo.get_der(), clave))
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
            sucesor = self._minimo(nodo.get_der())
            nodo._Nodo__clave = sucesor.get_clave()
            nodo.set_der(self._suprimir(nodo.get_der(), sucesor.get_clave()))
        return nodo

    def _minimo(self, nodo):
        """Devuelve el nodo con clave mínima"""
        actual = nodo
        while actual.get_izq() is not None:
            actual = actual.get_izq()
        return actual

    def inorden(self):
        """Recorrido en inorden (izq, raíz, der)"""
        print("Recorrido Inorden:")
        self._inorden(self.__raiz)
        print()

    def _inorden(self, nodo):
        if nodo:
            self._inorden(nodo.get_izq())
            print(nodo.get_clave(), end=" ")
            self._inorden(nodo.get_der())

    def preorden(self):
        """Recorrido en preorden (raíz, izq, der)"""
        print("Recorrido Preorden:")
        self._preorden(self.__raiz)
        print()

    def _preorden(self, nodo):
        if nodo:
            print(nodo.get_clave(), end=" ")
            self._preorden(nodo.get_izq())
            self._preorden(nodo.get_der())

    def postorden(self):
        """Recorrido en postorden (izq, der, raíz)"""
        print("Recorrido Postorden:")
        self._postorden(self.__raiz)
        print()

    def _postorden(self, nodo):
        if nodo:
            self._postorden(nodo.get_izq())
            self._postorden(nodo.get_der())
            print(nodo.get_clave(), end=" ")

    def altura(self):
        """Devuelve la altura del árbol"""
        return self._altura(self.__raiz)

    def _altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura(nodo.get_izq()), self._altura(nodo.get_der()))
