class Moto:
    def __init__(self, cilindraje, modelo, color, peso):
        self.cilindraje = cilindraje
        self.modelo = modelo
        self.color = color
        self.peso = peso
    
    def __str__(self):
        return f"{self.modelo} - Cilindraje: {self.cilindraje}, Color: {self.color}, Peso: {self.peso}"

class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def agregar_arista(self, moto_origen, moto_destino):
        if moto_origen not in self.grafo:
            self.grafo[moto_origen] = []
        if moto_destino not in self.grafo:
            self.grafo[moto_destino] = []
        self.grafo[moto_origen].append(moto_destino)
    
    def __str__(self):
        return '\n'.join([f"{moto}: {', '.join(map(str, vecinos))}" for moto, vecinos in self.grafo.items()])

def dfs(grafo, inicio, propiedad_filtro, valor_filtro, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    
    if getattr(inicio, propiedad_filtro) == valor_filtro:
        print(inicio)  # Imprimir el nodo si coincide con el filtro
    
    for vecino in grafo[inicio]:
        if vecino not in visitados:
            dfs(grafo, vecino, propiedad_filtro, valor_filtro, visitados)
    
    return visitados

# Crear el grafo
grafo = Grafo()

# Crear instancias de Moto
moto1 = Moto(cilindraje=250, modelo="Yamaha FZ", color="Negro", peso=150)
moto2 = Moto(cilindraje=400, modelo="Honda CB", color="Rojo", peso=180)
moto3 = Moto(cilindraje=250, modelo="Suzuki Gixxer", color="Azul", peso=160)

# Agregar aristas al grafo
grafo.agregar_arista(moto1, moto2)
grafo.agregar_arista(moto1, moto3)

# Ejecutar DFS con filtro por cilindraje igual a 250
print("Motos con cilindraje igual a 250:")
dfs(grafo.grafo, moto1, "cilindraje", 250)
