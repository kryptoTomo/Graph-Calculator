import random
import numpy as np
from Representation import *
from Generator import *

page_range_data={'name': 'Rysunek.png',
              'size': (6,6),
              'directed_all': True,
              'node_size': 500,
              'graph':{'A' : ['E' , 'F' , 'I'],
                       'B' : ['A' , 'C' , 'F'],
                       'C' : ['B' , 'D' , 'E' , 'L'],
                       'D' : ['C' , 'E' , 'H' , 'I' , 'K'],
                       'E' : ['C' , 'G' , 'H' , 'I'],
                       'F' : ['B' , 'G'],
                       'G' : ['E' , 'F' , 'H'],
                       'H' : ['D' , 'G' , 'I' , 'L'],
                       'I' : ['D' , 'E' , 'H' , 'J'],
                       'J' : ['I'],
                       'K' : ['D' , 'I'],
                       'L' : ['A' , 'H']
               },
               'nodes_description': {},
               'edges_description': {}
}

def page_rank_random_wandering(di_graph,d,n):
    di_graph=di_graph.toAdjacencyList()
    ranks = {i: 0 for i in di_graph.graph.keys()}
    v = random.choice(list(di_graph.graph.keys()))
    for i in range(n):
        rand = random.uniform(0, 1)
        ranks[v] += 1
        if rand < 1-d:
            v = random.choice(list(di_graph.graph[v]))
        else:
            v = random.choice(list(di_graph.graph.keys()))
    return {key: value / n for key, value in ranks.items()}

def page_rank_vector_iteration(di_graph,d,epsilon=10**(-30)):
    di_graph=di_graph.toAdjacencyMatrix()

    ranks = np.full(len(di_graph.graph), 1/len(di_graph.graph))

    P = [[] for i in range(len(di_graph.graph))]

    for i in range(len(di_graph.graph)):
        for j in range(len(di_graph.graph)):
            P[i].append((1 - d) * (di_graph.graph[i][j] / sum(di_graph.graph[i])) + d / len(di_graph.graph))

    P = np.array(P)

    error=1
    iteration=0

    while error>10**(-30):
        ranks_prev=ranks
        ranks = ranks @ P
        error=0
        iteration+=1
        for i in range(len(ranks)):
            error+=(ranks[i]-ranks_prev[i])**2

    print(error,iteration)
    return {i : ranks[i] for i in range(len(ranks))}

di_graph=AdjacencyList(page_range_data)
di_graph.graphVisualization()
# print(page_rank_random_wandering(di_graph, 0.15,1000000))
# print(page_rank_vector_iteration(di_graph, 0.15))
