# ============================================================
    # a) Mostrar el nodo padre y el nodo hermano
    # ============================================================

    def mostrar_padre_y_hermano(self, clave):
        """Muestra el padre y el hermano de un nodo dado."""
        padre = None
        actual = self.__raiz

        while actual and actual.get_clave() != clave:
            padre = actual
            if clave < actual.get_clave():
                actual = actual.get_izq()
            else:
                actual = actual.get_der()

        if actual is None:
            print(f"El nodo {clave} no existe en el árbol.")
            return

        if padre is None:
            print(f"El nodo {clave} es la raíz, no tiene padre ni hermano.")
            return

        print(f"Padre del nodo {clave}: {padre.get_clave()}")

        # Buscar el hermano
        if padre.get_izq() and padre.get_izq() != actual:
            print(f"Hermano del nodo {clave}: {padre.get_izq().get_clave()}")
        elif padre.get_der() and padre.get_der() != actual:
            print(f"Hermano del nodo {clave}: {padre.get_der().get_clave()}")
        else:
            print(f"El nodo {clave} no tiene hermano.")

    # ============================================================
    # b) Mostrar la cantidad de nodos (recursivo)
    # ============================================================

    def contar_nodos(self):
        """Devuelve la cantidad total de nodos del árbol."""
        return self._contar_nodos(self.__raiz)

    def _contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.get_izq()) + self._contar_nodos(nodo.get_der())

    # ============================================================
    # c) Mostrar la altura del árbol
    # ============================================================

    def altura(self):
        """Devuelve la altura del árbol."""
        return self._altura(self.__raiz)

    def _altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura(nodo.get_izq()), self._altura(nodo.get_der()))

    # ============================================================
    # d) Mostrar los sucesores de un nodo dado
    # ============================================================

    def mostrar_sucesores(self, clave):
        """Muestra los sucesores (hijos) del nodo con la clave dada."""
        nodo = self.buscar(clave)
        if nodo is None:
            print(f"El nodo {clave} no existe en el árbol.")
            return

        if nodo.get_izq():
            print(f"Sucesor izquierdo de {clave}: {nodo.get_izq().get_clave()}")
        else:
            print(f"El nodo {clave} no tiene sucesor izquierdo.")

        if nodo.get_der():
            print(f"Sucesor derecho de {clave}: {nodo.get_der().get_clave()}")
        else:
            print(f"El nodo {clave} no tiene sucesor derecho.")
