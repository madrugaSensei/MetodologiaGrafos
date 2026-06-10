import networkx as nx
import matplotlib.pyplot as plt
import random as r
import time 
import math

r.seed(time.time())

G = nx.Graph()
N = int(input("Digite o número de elementos no grafo: "))
v = list(range(1,N+1))
p = float(input("Digite a probabilidade: "))

# geração de grafos aleátorios não-direcionados por probabilidade
for i in v:
    G.add_node(i)

for i in v:
    for j in v:
        if j !=i and i > j:
            if r.random()<=p:
                G.add_edge(i, j)

# calculo da soma dos graus dos vertices
sum = 0
for i in v:
    sum += G.degree(i)

# número esperado de arestas
ea = p*(N*(N-1))/2
# media de arestas por nós
k = 1/N * sum
# grau médio
gm = (2*ea)/N
# mudança de fase
mf = 1/N
# probabilidade critica
pc = math.log(N)/N
# probabilidade de um grafo ter o grau médio
pgm = (gm**k*10**-gm)/math.factorial(int(k))
# distribuição de Binomial
b = p(N - 1)

# imprime os calculos
print(f"Número esperado de arestas: {ea}")
print(f"Grau médio: {gm}")
print(f"Probabilidade de um vértice ter o grau {gm}: {pgm}")
print(f"Média de arestas por nó: {k}")
print(f"Mudança de fase: {mf}")
print(f"Probabilidade crítica: {pc}")

# renderiza os grafos
nx.draw(G, with_labels=True, node_size=200)
plt.show()

#for i in v:
    #print(G.degree(i))

