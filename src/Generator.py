import random 
from Representation import AdjacencyList
import math

class Generator:
    @staticmethod
    def rand_graph_edge_number(n, l):
        data={'name': 'randomGraphEdgeNumber.png','size': (6, 6),'directed_all': False,'node_size': 500,'graph':{},'nodes_description':{},'edges_description':{}}
        if l > n*(n-1)/2:
            raise ValueError("Invalid number of nodes and edges")
        for i in range(n):
            data['graph'][i]=[]
        edges_count=0
        while edges_count<l:
            edge=tuple(random.sample(range(n), 2))
            if edge[0] not in data['graph'][edge[1]]: 
                data['graph'][edge[0]].append(edge[1])
                data['graph'][edge[1]].append(edge[0])
                edges_count+=1
        print(data)
        return AdjacencyList(data)

    @staticmethod
    def rand_graph_edge_probability(n, p):
        data={'name': 'randGraphEdgeProbability.png','size': (6, 6),'directed_all': False,'node_size': 500,'graph':{},'nodes_description':{},'edges_description':{}}
        for i in range(n):
            data['graph'][i]=[]
        for i in range(n):
            for j in range(n):
                if i!=j and random.random() <= p and j not in data['graph'][i]:
                    data['graph'][i].append(j)
                    data['graph'][j].append(i)
        return AdjacencyList(data)

    @staticmethod
    def rand_digraph_edge_number(n, l):
        data={'name': 'randomDigraphEdgeNumber.png','size': (6, 6),'directed_all': False,'node_size': 500,'graph':{},'nodes_description':{},'edges_description':{}}
        if l > math.factorial(n-1) :
            raise ValueError("Invalid number of nodes and edges")
        for i in range(n):
            data['graph'][i]=[]
            data['nodes_description'][i]={'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))}

        edges_count=0
        while edges_count<l:
            edge=tuple(random.sample(range(n), 2))
            if edge[0] not in data['graph'][edge[1]]: 
                data['graph'][edge[0]].append(edge[1])
                data['graph'][edge[1]].append(edge[0])
                data['edges_description'][(edge[0],edge[1])]={'weight': random.randint(0,99),'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint (0,255),random.randint(0,255)) ,'directed': random.sample([True,False],1)[0]}
                edges_count+=1
        print(data)
        return AdjacencyList(data)
    @staticmethod
    def rand_digraph_edge_probability(n, p):
        data={'name': 'randDigraphEdgeProbability.png','size': (6, 6),'directed_all': False,'node_size': 500,'graph':{},'nodes_description':{},'edges_description':{}}
        for i in range(n):
            data['graph'][i]=[]
            data['nodes_description'][i]={'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))}
        for i in range(n):
            for j in range(n):
                if i!=j and random.random() <= p and j not in data['graph'][i]:
                    data['graph'][i].append(j)
                    data['graph'][j].append(i)
                    data['edges_description'][(i,j)]={'weight': random.randint(0,99),'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint (0,255),random.randint(0,255)) ,'directed': random.sample([True,False],1)[0]}
        return AdjacencyList(data)

# Generator.rand_graph_edge_number(10, 5).graphVisualization()
# Generator.rand_graph_edge_probability(10, 0.5).graphVisualization()
# Generator.rand_digraph_edge_number(10, 5).graphVisualization()
# Generator.rand_digraph_edge_probability(10, 0.5).graphVisualization()