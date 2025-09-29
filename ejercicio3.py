import heapq  # para manejar la cola de prioridad

class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izq = None
        self.der = None

    # comparación necesaria para usar heapq
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia


class Huffman:
    def __init__(self):
        self.codigos = {}  # tabla de códigos generados
        self.raiz = None

    # ----------------------------------------------------
    # 1️⃣ Calcular frecuencia de cada carácter
    # ----------------------------------------------------
    def calcular_frecuencias(self, texto):
        frecuencias = {}
        for caracter in texto:
            frecuencias[caracter] = frecuencias.get(caracter, 0) + 1
        return frecuencias

    # ----------------------------------------------------
    # 2️⃣ Construir el árbol de Huffman
    # ----------------------------------------------------
    def construir_arbol(self, frecuencias):
        heap = []
        for caracter, freq in frecuencias.items():
            heapq.heappush(heap, NodoHuffman(caracter, freq))

        while len(heap) > 1:
            nodo1 = heapq.heappop(heap)
            nodo2 = heapq.heappop(heap)
            nuevo = NodoHuffman(None, nodo1.frecuencia + nodo2.frecuencia)
            nuevo.izq = nodo1
            nuevo.der = nodo2
            heapq.heappush(heap, nuevo)

        self.raiz = heap[0]

    # ----------------------------------------------------
    # 3️⃣ Generar los códigos de Huffman
    # ----------------------------------------------------
    def generar_codigos(self):
        def recorrer(nodo, codigo_actual):
            if nodo is None:
                return
            if nodo.caracter is not None:  # es hoja
                self.codigos[nodo.caracter] = codigo_actual
                return
            recorrer(nodo.izq, codigo_actual + "0")
            recorrer(nodo.der, codigo_actual + "1")

        recorrer(self.raiz, "")

    # ----------------------------------------------------
    # 4️⃣ Codificar texto
    # ----------------------------------------------------
    def codificar(self, texto):
        return ''.join(self.codigos[car] for car in texto)

    # ----------------------------------------------------
    # 5️⃣ Decodificar texto (opcional)
    # ----------------------------------------------------
    def decodificar(self, texto_codificado):
        resultado = ""
        nodo = self.raiz
        for bit in texto_codificado:
            if bit == "0":
                nodo = nodo.izq
            else:
                nodo = nodo.der
            if nodo.caracter is not None:
                resultado += nodo.caracter
                nodo = self.raiz
        return resultado

if __name__ == "__main__":
    # Leer el archivo de texto
    nombre_archivo = "texto.txt"
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        texto = f.read()

    print("Texto original:\n", texto)
    print("\nLongitud original:", len(texto), "caracteres\n")

    h = Huffman()

    # 1️⃣ Calcular frecuencias
    frecuencias = h.calcular_frecuencias(texto)
    print("Frecuencias de caracteres:")
    for c, f in frecuencias.items():
        print(repr(c), ":", f)

    # 2️⃣ Construir el árbol
    h.construir_arbol(frecuencias)

    # 3️⃣ Generar códigos
    h.generar_codigos()
    print("\nCódigos de Huffman:")
    for c, cod in h.codigos.items():
        print(repr(c), "→", cod)

    # 4️⃣ Codificar texto
    texto_codificado = h.codificar(texto)
    print("\nTexto comprimido:\n", texto_codificado)
    print("\nLongitud comprimida:", len(texto_codificado), "bits")

    # 5️⃣ Decodificar (verificación)
    decodificado = h.decodificar(texto_codificado)
    print("\nTexto decodificado:\n", decodificado)
