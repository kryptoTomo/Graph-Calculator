import networkx as nx
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
import copy
import random



example_data={'name': 'Rysunek.png',
              'size': (10,10),
              'directed_all': True,
              'node_size': 500,
              'graph':{0:  [1,4,5], 
                       1:  [0,2,5], 
                       2:  [1,3,4,11], 
                       3:  [2,7,8,10], 
                       4:  [0,2,6,8], 
                       5:  [0,1,6], 
                       6:  [4,5,7], 
                       7:  [3,6,8,11], 
                       8:  [3,4,7,0], 
                       9:  [8], 
                       10: [3], 
                       11: [2,7]
               },
               'nodes_description': {},
               'edges_description': {(0,1): {'weight': 1,'color': ''},
                            (1, 0): {'weight': 2,'color': ''}
        }  
}

class GraphRepresentation:
    def __init__(self, data):
        self.graph=data['graph']
        self.name=data['name']
        self.size=data['size']
        self.node_size=data['node_size']
        self.directed_all=data['directed_all']
        self.nodes_description=data['nodes_description']
        self.edges_description=data['edges_description']
        self.edges=[]

    def graphVisualization(self):
        plt.figure(figsize=self.size)

        if self.directed_all:
            G = nx.DiGraph()
        else:
            G = nx.Graph()

        G.add_nodes_from(range(len(self.graph)))
        G.add_edges_from(self.edges)

        node_colors=list(i['color']  for i in self.nodes_description.values())

        pos = nx.circular_layout(G)

        nx.draw_networkx_nodes(G, pos, node_size = self.node_size)
        nx.draw_networkx_nodes(G, pos, nodelist= list(self.nodes_description.keys()), node_color = node_colors, node_size = self.node_size)

        nx.draw_networkx_labels(G, pos)

        nx.draw_networkx_edges(G, pos, arrows=self.directed_all)

        nx.draw_networkx_edge_labels(G, pos, edge_labels={ i[0]: i[1]['weight'] for i in self.edges_description.items()},label_pos = 0.2 if self.directed_all else 0.4,font_size=9)

        plt.savefig(f'src/__imgcache__/{self.name}')
        plt.close()
        # plt.show()

    def toAdjacencyList(self):
        data={}
        data['name']=copy.deepcopy(self.name)
        data['size']=copy.deepcopy(self.size)
        data['node_size']=copy.deepcopy(self.node_size)
        data['directed_all']=copy.deepcopy(self.directed_all)
        data['nodes_description']=copy.deepcopy(self.nodes_description)
        data['edges_description']=copy.deepcopy(self.edges_description)

        print(self.edges)

        graph={}

        for i in range(len(self.graph)):
            graph[i]=[]

        for edge in self.edges:
            graph[edge[0]].append(edge[1])

        data['graph']=copy.deepcopy(graph)

        return data

    def toAdjacencyMatrix(self):
        data={}
        data['name']=copy.deepcopy(self.name)
        data['size']=copy.deepcopy(self.size)
        data['node_size']=copy.deepcopy(self.node_size)
        data['directed_all']=copy.deepcopy(self.directed_all)
        data['nodes_description']=copy.deepcopy(self.nodes_description)
        data['edges_description']=copy.deepcopy(self.edges_description)

        print(self.edges)

        graph=[ [0 for _ in range(len(self.graph)) ] for _ in range(len(self.graph)) ]

        for edge in self.edges:
            graph[edge[0]][edge[1]] = 1

        data['graph']=copy.deepcopy(graph)

        return data
    def toIncidentMatrix(self):
        data={}
        data['name']=copy.deepcopy(self.name)
        data['size']=copy.deepcopy(self.size)
        data['node_size']=copy.deepcopy(self.node_size)
        data['directed_all']=copy.deepcopy(self.directed_all)
        data['nodes_description']=copy.deepcopy(self.nodes_description)
        data['edges_description']=copy.deepcopy(self.edges_description)
        
        edges=copy.deepcopy(self.edges)
        for edge in edges:
            if (edge[1],edge[0]) in edges:
                edges.remove((edge[1],edge[0]))

        graph=[[0 for _ in range(len(edges))] for _ in range(len(self.graph)) ]

        print(self.edges)

        for i in range(len(edges)):
            graph[edges[i][0]][i]=1
            graph[edges[i][1]][i]=1

        data['graph']=copy.deepcopy(graph)

        return data

####################AdjacencyList####################

class AdjacencyList (GraphRepresentation):
    def __init__(self, data):
        super().__init__(data)

        self.normalization={j: int(i) for i,j in enumerate(self.graph.keys())}

        if self.directed_all:
            for edge in self.graph.items():
                self.edges.extend( [ (self.normalization[edge[0]],self.normalization[x]) for x in edge[1]] )
        else:
            for edge in self.graph.items():
                self.edges.extend( [ (self.normalization[edge[0]],self.normalization[x]) for x in edge[1] if x>edge[0]] )

    def printGraph(self):
        # print('Adjacency List ', end='\n\n')

        returnStr=""
        for i,j in self.graph.items():
            returnStr+=str((str(i)+': ').ljust(5)  + str(j))+"\n"
            # print( (str(i)+': ').ljust(5)  + str(j) )
        return returnStr

    def toAdjacencyList(self):
        return self
    def toAdjacencyMatrix(self):
        return AdjacencyMatrix(super().toAdjacencyMatrix())
    def toIncidentMatrix(self):
        return IncidentMatrix(super().toIncidentMatrix())

####################AdjacencyMatrix####################

class AdjacencyMatrix (GraphRepresentation):
    def __init__(self, data):
        super().__init__(data)

        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if self.graph[i][j]==1:
                    self.edges.append( (i,j) )

    def printGraph(self):
        # print('Adjacency Matrix ', end='\n\n')

        returnStr=""
        for i in self.graph:
            returnStr+=str(i)+"\n"
            # print(i)
        return returnStr

    def toAdjacencyList(self):
        return AdjacencyList(super().toAdjacencyList())
    def toAdjacencyMatrix(self):
        return self
    def toIncidentMatrix(self):
        return IncidentMatrix(super().toIncidentMatrix())

####################IncidentMatrix####################

class IncidentMatrix (GraphRepresentation):
    def __init__(self, data):
        super().__init__(data)

        for i in range(len(self.graph[0])):
            edge=[]
            for j in range(len(self.graph)):
                if self.graph[j][i]!=0 :
                    edge.append(j)
            self.edges.append(tuple(edge))

    def printGraph(self):
        # print('Adjacency Matrix ', end='\n\n')

        returnStr=""
        for i in self.graph:
            returnStr+=str(i)+"\n"
            # print(i)
        return returnStr

    def toAdjacencyList(self):
        return AdjacencyList(super().toAdjacencyList())
    def toAdjacencyMatrix(self):
        return AdjacencyMatrix(super().toAdjacencyMatrix())
    def toIncidentMatrix(self):
        return self