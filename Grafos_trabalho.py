class grafo:

    def __init__(self, dicionario_grafo=None):
        if dicionario_grafo is None:
            dicionario_grafo = {}
        self.dicionario_grafo = dicionario_grafo


    def get_vertices(self):#Mostra todas os vertices NÃO orientado
        return list(self.dicionario_grafo.keys())

    def find_edges(self):#Printa todas as arestas NÃO orientado
        edge_name = []
        for vertex in self.dicionario_grafo:
            for next_vertex in self.dicionario_grafo[vertex]:
                if {next_vertex, vertex} not in edge_name:
                    edge_name.append({next_vertex, vertex})

        return edge_name

    def add_vertice(self, vertice):#NÃO orientado
        if vertice not in self.dicionario_grafo:
            self.dicionario_grafo[vertice] = []

    def remove_vertice(self, vertice):#Remove vertice NÃO ORIENTADO
        del self.dicionario_grafo[vertice]

    def add_aresta(self, aresta):#NÃO orientado
        aresta = set(aresta)
        (vertex_1, vertex_2) = tuple(aresta)
        if vertex_1 in self.dicionario_grafo:
            self.dicionario_grafo[vertex_1].append(vertex_2)
        else:
            self.dicionario_grafo[vertex_1] = [vertex_2]



    def print_grafo_lista(self):#printa a lista de adjacencia para grafos NÃO orientados
        for item in self.dicionario_grafo.items():
            print(item)

    def print_grafo_matriz(self):#Printa a matrix de adjancia para grafos NÃO orientados (falta colocar um end line a cada linha)
        keys = sorted(graph.keys())
        size = len(keys)
        matrix = [[0] * size for i in range(size)]
        # We iterate over the key:value entries in the dictionary first,
        # then we iterate over the elements within the value
        for a, b in [(keys.index(a), keys.index(b))
            for a, row in graph.items() for b in row]:
            # Use 1 to represent if there's an edge
            # Use 2 to represent when node meets itself in the matrix (A -> A)
            matrix[a][b] = 2 if (a == b) else 1
        print(matrix)

# Create the dictionary with graph elements
graph = {
            'a': ['b', 'c'],
            'b': ['c', 'd', 'e'],
            'c': ['d'],
            'd': ['e'],
            'e': []
    }

grafo_direcionado = {
            'a': [],
            'b': ['a', 'e'],
            'c': ['a', 'b', 'd'],
            'd': ['b'],
            'e': ['b', 'd']
    }

g = grafo(graph)
d = grafo(grafo_direcionado)

#print(g.get_vertices())
print(d.get_vertices())
#print(g.print_grafo_lista())
print(d.remove_vertice('b'))
print(d.get_vertices())
d.add_vertice('f')
print(d.get_vertices())


# def le_txt(self, dados):
#     self.dados = dados
#     if os.path.isfile('grafo.txt'):  # Verifica se o arquivo esá OK
#         file = open('grafo.txt', 'r')
# 
#         for i in file.readlines():  # Itera por todas as linhas do arquivo
#             graph = i.strip().split(' ')  # Da o split se contém 1/2 espaços
#             self.dados.append(graph[0])
#         print(dados)
#     return self.dados


