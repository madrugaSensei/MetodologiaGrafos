import networkx as nx
import matplotlib.pyplot as plt
import random as r
import time 
import math

r.seed(time.time())

G = nx.Graph()
N = int(input("Digite o número de elementos no grafo: "))
v = list(range(1,N))
m = float(input("Digite a quantidade de arestas: "))

# geração de grafos aleátorios não-direcionados por número de arestas
for i in v:
    G.add_node(i)

# Calcula o limite máximo de arestas para um grafo simples
max_arestas = (N * (N - 1)) // 2
    
if m > max_arestas:
    raise ValueError(f"O número de arestas não pode exceder {max_arestas} para {N} vértices.")

    # Adiciona as arestas aleatoriamente até chegar no valor desejado
while G.number_of_edges() < m:
    u = r.randint(0, N - 1)
    z = r.randint(0, N - 1)
        
    # Evita laços (aresta ligada ao mesmo vértice) e arestas duplicadas
    if u != z and not G.has_edge(u, z):
        G.add_edge(u, z)

# calculo da soma dos graus dos vertices
sum = 0
for i in v:
    sum += G.degree(i)

# media de arestas por nós
k = 1/N * sum
# grau médio
gm = (2*m)/N
# mudança de fase
mf = 1/N
# probabilidade critica
pc = math.log(N)/N
# probabilidade de reaparecimento
pr = 1/math.factorial(N)/math.factorial(2)*math.factorial(N-2)

# imprime os calculos
print(f"Grau médio: {gm}")
print(f"Média de vertices: {k}")
print(f"Mudança de fase: {mf}")
print(f"Probabilidade crítica: {pc}")
print(f"Probabilidade de reaparecimento: {pr}")

# renderiza os grafos
nx.draw(G, with_labels=True, node_size=200)
plt.show()