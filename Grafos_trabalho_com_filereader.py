from collections import defaultdict

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

    def grafo_transposto(self):#Tem que verificar se essa função está de correta, é pra ser utilizada nos grafos que são Direcionados, né? Faça testes mudando 
        output = {}                                 #direto lá no diciionário 'grafo_direcionado' pra ver se o output está de acordo com a definição de transposto
        for e, v in self.dicionario_grafo.items(): # chris: Mexi aqui pra ele ler o grafo pra cada grafo que tu colocar
            output[e] = sorted(v, reverse=False) #chris: descobri que essa é o exercicio 9, e ela ta errada, vou deixar de recordação ai e depois a gente apaga, a certa é a função abaixo V
        print(output)

    def transpor_grafo(self): #usar somente com grafo direcionado
        if Grafo_Direcionado_Boolean == False: #caso não for direcionado retorna
            print()
            print("Não se pode utilizar essa função com um grafo não direcionado (ou undirected).")
            print()
            return
        graph_trans = defaultdict(list)
        for source, targets in self.dicionario_grafo.items(): 
            for target in targets: 
                graph_trans[target].append(source)
        graph_trans = dict(graph_trans)
        print(graph_trans)     

    def graph_complement(self):
        #transpõe o grafo, pra ele ficar com todas as chaves e não dar erro, ISSO É UM WORKAROUND COM UMA FUNÇÃO QUE EU JÁ TINHA E NÃO FOI TESTADO DEVIDAMENTE
        graph_trans = defaultdict(list)
        for source, targets in self.dicionario_grafo.items(): 
            for target in targets: 
                graph_trans[target].append(source)
        graph_trans = dict(graph_trans)
        #complementa o grafo transposto
        complement = {}
        for u in graph_trans:
            complement[u] = set(graph_trans.keys()) - set(graph_trans[u]) - {u}
        print(complement)
        return complement


# Create the dictionary with graph elements
graph = {
            'a': ['b', 'c'],
            'b': ['c', 'd', 'e'],
            'c': ['d'],
            'd': ['e'],
            'e': []
    }

grafo_complemento_de_graph = {
            'a': ['d'],
            'b': [],
            'c': [],
            'd': [],
            'e': ['e']
    }

graph_completo = {
            'a': ['b', 'c', 'd'],
            'b': ['c', 'd', 'e'],
            'c': ['d'],
            'd': ['e'],
            'e': ['a']
    }

grafo_direcionado = {
            'a': [],
            'b': ['a', 'e'],
            'c': ['a', 'b', 'd'],
            'd': ['b'],
            'e': ['b', 'd']
    }

def dic_read_append(arquivo):
    lista_arquivo = open(arquivo,"r").readlines() # Lê o arquivo e usa a readline pra transformar em lista e não em TextIOWrapper
    if 'undirected' in open(arquivo).read(): # Verifica no arquivo inteiro se tem a string 'undirected'
        Grafo_Direcionado_Boolean = False #se houver, coloca a variavel "Grafo_Direcionado_Boolean" como falso
        lista_arquivo.pop(0) #Pula a primeira linha (linha do directed ou undirected)
        dicionario = defaultdict(list) # Instancia o dicionário antes dos loops
        for line in lista_arquivo: #para cada linha na lista de arquivos, faz V
            key, value = line.strip().split(" ") # Separa cada linha em dois valores (chave e valor) usando o Split(" ") para separar o espaço e o strip() para remover qualquer espaçamento
            dicionario[key].append(value) # Acrescenta os valores no dicionário sem escrever por cima
        for key, lista in list(dicionario.items()): #para as variáveis key e lista na lista do dicionário, faz V
            for value in lista: # para cada valor em I faz V
                if key not in dicionario[value]: # se a chave nao estiver no dicionario, faz V
                    dicionario[value].append(key) # Acrescenta a chave nos valores
        dicionario = dict(dicionario) #passa a variável dict para lista
        return dicionario, Grafo_Direcionado_Boolean #retorna duas variáveis
    else:
        Grafo_Direcionado_Boolean = True #se não houver, coloca a variavel "Grafo_Direcionado_Boolean" como true
        lista_arquivo.pop(0) #Pula a primeira linha
        dicionario = defaultdict(list) # Instancia o dicionário
        for line in lista_arquivo: #para cada linha na lista de arquivos, faz V
            key, value = line.strip().split(" ") # Separa cada linha em dois valores (chave e valor) usando o Split(" ") para separar o espaço e o strip() para remover qualquer espaçamento
            dicionario[key].append(value) # Acrescenta os valores no dicionário sem escrever por cima
        dicionario = dict(dicionario) #passa a variável dict para lista
        return dicionario, Grafo_Direcionado_Boolean #retorna duas variáveis

grafos, Grafo_Direcionado_Boolean = dic_read_append('grafos1.txt')
#print(Grafo_Direcionado_Boolean)

g = grafo(grafos)

#Me parece que ao usar a função find_edge com um grafo DIRECIONADO ela já me retorna
#o grafo transposto!!! Confere isso ai
#chris: às vezes retorna, às vezes não, bizarro

print()
print('Grafo: ')
g.print_grafo_lista()
print()
print('Grafo transposto:')
g.transpor_grafo()
print('O grafo é direcionado?: ', Grafo_Direcionado_Boolean)
print()
print('Complemento do Grafo: ')
g.graph_complement()
print()