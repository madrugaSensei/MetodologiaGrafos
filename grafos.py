import networkx as nx
import matplotlib.pyplot as plt
import random as r
import time

r.seed(time.time())

G = nx.Graph()
N = 15
v = list(range(1,N+1))
p = 1/2

for i in v:
    G.add_node(i)

for i in v:
    for j in v:
        if j !=i and i > j:
            if r.random()<=p:
                G.add_edge(i, j)

sum = 0
k = 0
for i in v:
    sum += G.degree(i)

k = 1/N * sum

print(k)

nx.draw(G, with_labels=True, node_size=2000)
plt.show()

#for i in v:
    #print(G.degree(i))

