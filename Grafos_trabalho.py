class grafo:

    def __init__(self, dicionario_grafo=None):
        if dicionario_grafo is None:
            dicionario_grafo = {}
        self.dicionario_grafo = dicionario_grafo

    def get_vertices(self):#Mostra todas os vertices
        return list(self.dicionario_grafo.keys())

    def find_edges(self):#Printa todas as arestas
        edge_name = []
        for vertex in self.dicionario_grafo:
            for next_vertex in self.dicionario_grafo[vertex]:
                if {next_vertex, vertex} not in edge_name:
                    edge_name.append({next_vertex, vertex})

        return edge_name

    def add_vertice(self, vertice):
        if vertice not in self.dicionario_grafo:
            self.dicionario_grafo[vertice] = []

    def add_aresta(self, aresta):
        aresta = set(aresta)
        (vertex_1, vertex_2) = tuple(aresta)
        if vertex_1 in self.dicionario_grafo:
            self.dicionario_grafo[vertex_1].append(vertex_2)
        else:
            self.dicionario_grafo[vertex_1] = [vertex_2]


# Create the dictionary with graph elements
graph = {
            'a': ['b', 'c'],
            'b': ['c', 'd', 'e'],
            'c': ['d'],
            'd': ['e'],
            'e': []
    }


g = grafo(graph)

print(g.get_vertices())
g.add_vertice("f")
print(g.get_vertices())



