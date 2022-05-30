import random 
from Representation import AdjacencyList
import math
import networkx as nx

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
        return AdjacencyList(data)

    @staticmethod
    def rand_graph_edge_probability(n, p):
        data={'name': 'randomGraphEdgeProbability.png','size': (6, 6),'directed_all': False,'node_size': 500,'graph':{},'nodes_description':{},'edges_description':{}}
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
        data={'name': 'randomDigraphEdgeNumber.png','size': (6, 6),'directed_all': True,'node_size': 500,'graph':{},'nodes_description':{},'edges_description':{}}
        if l > n*(n-1):
            raise ValueError("Invalid number of nodes and edges")
        for i in range(n):
            data['graph'][i]=[]
            data['nodes_description'][i]={'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))}

        edges_count=0
        while edges_count<l:
            edge=tuple(random.sample(range(n), 2))
            if edge[0] not in data['graph'][edge[1]]: 
                data['graph'][edge[1]].append(edge[0])
                edges_count+=1
                data['edges_description'][(edge[1],edge[0])]={'weight': random.randint(0,15),'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint (0,255),random.randint(0,255))}
        return AdjacencyList(data)

    @staticmethod
    def rand_digraph_edge_probability(n, p):
        data={'name': 'randomDigraphEdgeProbability.png','size': (6, 6),'directed_all': True,'node_size': 500,'graph':{},'nodes_description':{},'edges_description':{}}
        for i in range(n):
            data['graph'][i]=[]
            data['nodes_description'][i]={'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))}
        for i in range(n):
            for j in range(n):
                if i!=j and random.random() <= p:
                    data['graph'][i].append(j)
                    data['edges_description'][(i,j)]={'weight': random.randint(-2,15),'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint (0,255),random.randint(0,255))}
        return AdjacencyList(data)
    @staticmethod
    def rand_undirected_consistent_graph(n):
        data={'name': 'randomUndirectedConsistentGraph.png','size': (6, 6),'directed_all': False,'node_size': 500,'graph':{},'nodes_description':{},'edges_description':{}}
        g = nx.Graph()
        g.add_nodes_from(range(n))
        l=random.randint(1,n*(n-1)/2)
        for i in range(n):
            data['graph'][i]=[]
        edges_count=0
        while edges_count<l:
            edge=tuple(random.sample(range(n), 2))
            if edge[0] not in data['graph'][edge[1]]: 
                data['graph'][edge[0]].append(edge[1])
                data['graph'][edge[1]].append(edge[0])
                data['edges_description'][(edge[0],edge[1])]={'weight': random.randint(1,10),'color': ''}
                g.add_edge(edge[0],edge[1])
                edges_count+=1
        while not nx.is_connected(g):
            list_of_comps = list(nx.connected_components(g))
            random_node1 = random.sample(list(list_of_comps[1]), 1)[0]
            random_node2 = random.sample(list(list_of_comps[0]), 1)[0]
            g.add_edge(random_node1, random_node2)
            data['graph'][random_node1].append(random_node2)
            data['graph'][random_node2].append(random_node1)
            data['edges_description'][(random_node1,random_node2)]={'weight': random.randint(1,10),'color': ''}
        return AdjacencyList(data)
    @staticmethod
    def random_undirected_consistent_graph(n):
        data={'name': 'randomUndirectedConsistentGraph.png','size': (6, 6),'directed_all': False,'node_size': 500,'graph':{},'nodes_description':{},'edges_description':{}}
        g = nx.Graph()
        g.add_nodes_from(range(n))
        l=random.randint(1,n*(n-1)/2)
        for i in range(n):
            data['graph'][i]=[]
        edges_count=0
        while edges_count<l:
            edge=tuple(random.sample(range(n), 2))
            if edge[0] not in data['graph'][edge[1]]: 
                data['graph'][edge[0]].append(edge[1])
                data['graph'][edge[1]].append(edge[0])
                data['edges_description'][(edge[0],edge[1])]={'weight': random.randint(1,10),'color': '' ,'directed': False}
                edges_count+=1
                g.add_edge(edge[0],edge[1])
        while not nx.is_connected(g):
            list_of_comps = list(nx.connected_components(g))
            random_node1 = random.sample(list(list_of_comps[1]), 1)[0]
            random_node2 = random.sample(list(list_of_comps[0]), 1)[0]
            g.add_edge(random_node1, random_node2)
            data['graph'][random_node1].append(random_node2)
            data['graph'][random_node2].append(random_node1)
            data['edges_description'][(random_node1,random_node2)]={'weight': random.randint(1,10),'color': '' ,'directed': False}
        return AdjacencyList(data)
# Generator.rand_graph_edge_number(10, 5).graphVisualization()
# Generator.rand_graph_edge_probability(10, 0.5).graphVisualization()
# Generator.rand_digraph_edge_number(10, 5).graphVisualization()
# Generator.rand_digraph_edge_probability(10, 0.1).graphVisualization()
# Generator.rand_undirected_consistent_graph(10).graphVisualization()