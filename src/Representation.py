import networkx as nx
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
import copy
import random


example_data={'name': 'Rysunek.png',
              'size': (6,6),
              'directed_all': True,
              'node_size': 500,
              'graph':{1:  [2,5,6], 
                       2:  [1,3,6], 
                       3:  [2,4,5,12], 
                       4:  [3,8,9,11], 
                       5:  [1,3,7,9], 
                       6:  [1,2,7], 
                       7:  [5,6,8], 
                       8:  [4,7,9,12], 
                       9:  [4,5,8,10], 
                       10: [9], 
                       11: [4], 
                       12: [3,8]
               },
               'nodes_description':{1: {'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))},
                                    2: {'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))},
                                    3: {'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))},
                                    4: {'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))},
                                    5: {'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))},
                                    6: {'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))},
                                    7: {'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))},
                                    8: {'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))},
                                    9: {'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))},
                                    10: {'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))},
                                    11: {'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))}
        },
        'edges_description': {(0,1):  {'weight': random.randint(0,99),'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint (0,255),random.randint(0,255)) ,'directed': random.sample([True,False],1)} ,
                            (0, 4):  {'weight': random.randint(0,99),'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255)) ,'directed': random.sample([True,False],1)} ,
                            (0, 5):  {'weight': random.randint(0,99),'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255)) ,'directed': random.sample([True,False],1)} ,
                            (1, 2):  {'weight': random.randint(0,99),'color': '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255)) ,'directed': random.sample([True,False],1)}
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

        G = nx.Graph()

        G.add_nodes_from(range(len(self.graph)))
        G.add_edges_from(self.edges)

        node_colors=list(i['color'] for i in self.nodes_description.values())

        edges_description_directed={ i[0]: i[1] for i in self.edges_description.items() if i[1]['directed']}
        edges_description_no_directed={ i[0]: i[1] for i in self.edges_description.items() if not i[1]['directed']}

        pos = nx.circular_layout(G)

        nx.draw_networkx_nodes(G, pos, node_size = self.node_size)
        nx.draw_networkx_nodes(G, pos, nodelist= list(self.nodes_description.keys()), node_color = node_colors, node_size = self.node_size)

        nx.draw_networkx_labels(G, pos)

        if self.directed_all:
            nx.draw_networkx_edges(G, pos, edgelist=list(set(self.edges)-set(edges_description_directed.keys())),arrows = self.directed_all)
        else:
            nx.draw_networkx_edges(G, pos)

        nx.draw_networkx_edges(G, pos, edgelist=list(edges_description_directed.keys()), edge_color=[i['color'] for i in edges_description_directed.values()], arrows=True)

        nx.draw_networkx_edges(G, pos, edgelist=list(edges_description_no_directed.keys()), edge_color=[i['color'] for i in edges_description_no_directed.values()], arrows=False)

        nx.draw_networkx_edge_labels(G,pos,edge_labels={ i[0]: i[1]['weight'] for i in self.edges_description.items()})

        plt.savefig(f'src/__imgcache__/{self.name}')
        # plt.show()

    def toAdjacencyList(self):
        data={}
        data['name']=copy.deepcopy(self.name)
        data['size']=copy.deepcopy(self.size)
        data['node_size']=copy.deepcopy(self.node_size)
        data['directed_all']=copy.deepcopy(self.directed_all)
        data['nodes_description']=copy.deepcopy(self.nodes_description)
        data['edges_description']=copy.deepcopy(self.edges_description)

        graph={}

        for i in range(len(self.graph)):
            graph[i]=[]

        for edge in self.edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

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

        graph=[ [0 for _ in range(len(self.graph)) ] for _ in range(len(self.graph)) ]

        for edge in self.edges:
            graph[edge[0]][edge[1]] = 1
            graph[edge[1]][edge[0]] = 1

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

        graph=[[0 for _ in range(len(self.edges))] for _ in range(len(self.graph)) ]

        for i in range(len(self.edges)):
            graph[self.edges[i][0]][i]=1
            graph[self.edges[i][1]][i]=1

        data['graph']=copy.deepcopy(graph)

        return data

####################AdjacencyList####################

class AdjacencyList (GraphRepresentation):
    def __init__(self, data):
        super().__init__(data)

        self.normalization={j: int(i) for i,j in enumerate(self.graph.keys())}

        if self.directed_all:
            for edge in self.graph.items():
                self.edges.extend( [ (self.normalization[edge[0]],self.normalization[x]) for x in edge[1] if x>edge[0]] )
        else:
            for edge in self.graph.items():
                self.edges.extend( [ (self.normalization[edge[0]],self.normalization[x]) for x in edge[1]] )

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
            for j in range(i+1):
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