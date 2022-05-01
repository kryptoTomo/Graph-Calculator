import random 
from Representation import AdjacencyList

class Generator:
    @staticmethod
    def rand_graph_edge_number(n, l):
        data={'name': 'Ad3 (1).png','directed': True,'colors': [],'graph':{}}
        for i in range(n):
            data['graph'][i]=[]
        edges_count=0
        while edges_count<l:
            edge=tuple(random.sample(range(n), 2))
            if edge[0] not in data['graph'][edge[1]]: 
                data['graph'][edge[0]].append(edge[1])
                data['graph'][edge[1]].append(edge[0])
                edges_count+=1
        return AdjacencyList(data)

    @staticmethod
    def rand_graph_edge_probability(n, p):
        data={'name': 'Ad3 (2).png','directed': True,'colors': [],'graph':{}}
        for i in range(n):
            data['graph'][i]=[]
        for i in range(n):
            for j in range(n):
                if i!=j and random.random() <= p and j not in data['graph'][i]:
                    data['graph'][i].append(j)
                    data['graph'][j].append(i)
        return AdjacencyList(data)

# Generator.rand_graph_edge_number(10, 5).graphVisualization()
# Generator.rand_graph_edge_probability(10, 0.5).graphVisualization()