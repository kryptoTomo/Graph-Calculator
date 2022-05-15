from igraph import *
import copy

data1={'name': 'Ad1.png',
       'directed': True,
       'colors': [],
       'graph':{ 'a':  ['b','e','f'],
                 'b':  ['a','c','f'],
                 'c':  ['b','d','e','l'],
                 'd':  ['c','h','i','k'],
                 'e':  ['a','c','g','i'],
                 'f':  ['a','b','g'],
                 'g':  ['e','f','h'],
                 'h':  ['d','g','i','l'],
                 'i':  ['d','e','h','j'],
                 'j':  ['i'],
                 'k':  ['d'],
                 'l':  ['c','h']}
}

data2={'name': 'Ad1.png',
       'directed': True,
       'colors': [],
       'graph':{ 1:  [2,5,6],
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
                 12: [3,8]}
}
class GraphRepresentation:
    def __init__(self, data):
        self.name=data['name']
        self.directed=data['directed']
        self.colors=data['colors']
        self.graph=data['graph']
        self.edges=[]

    def graphVisualization(self):
        g = Graph()

        g.add_vertices(list(range(1,len(self.graph)+1)))
        g.add_edges(self.edges)

        g.vs["label"] = list(range(1,len(self.graph)+1))
        layout = g.layout_circle()

        visual_style = {}
        visual_style["vertex_size"] = 20
        visual_style["layout"] = layout
        visual_style["bbox"] = (800, 800)
        visual_style["margin"] = 20

        plot(g, **visual_style,target=f'src/__imgcache__/{self.name}')
        # out=plot(g, **visual_style)
        # out.save(self.name)

    def toAdjacencyList(self):
        data={}
        data['name']=copy.deepcopy(self.name)
        data['directed']=copy.deepcopy(self.directed)
        data['colors']=copy.deepcopy(self.colors)

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
        data['directed']=copy.deepcopy(self.directed)
        data['colors']=copy.deepcopy(self.colors)

        graph=[ [0 for _ in range(len(self.graph)) ] for _ in range(len(self.graph)) ]

        for edge in self.edges:
            graph[edge[0]][edge[1]] = 1
            graph[edge[1]][edge[0]] = 1

        data['graph']=copy.deepcopy(graph)

        return data
    def toIncidentMatrix(self):
        data={}
        data['name']=copy.deepcopy(self.name)
        data['directed']=copy.deepcopy(self.directed)
        data['colors']=copy.deepcopy(self.colors)

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

        if self.directed:
            for edge in self.graph.items():
                self.edges.extend( [ (self.normalization[edge[0]],self.normalization[x]) for x in edge[1] if x>edge[0]] )
        else:
            for edge in self.graph.items():
                self.edges.extend( [ (self.normalization[edge[0]],self.normalization[x]) for x in edge[1]] )

    def printGraph(self):
        print('Adjacency List ', end='\n\n')

        returnStr=""
        for i,j in self.graph.items():
            returnStr+=str((str(i)+': ').ljust(5)  + str(j))+"\n"
            print( (str(i)+': ').ljust(5)  + str(j) )
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
        print('Adjacency Matrix ', end='\n\n')

        returnStr=""
        for i in self.graph:
            returnStr+=str(i)+"\n"
            print(i)
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
        print('Adjacency Matrix ', end='\n\n')

        returnStr=""
        for i in self.graph:
            returnStr+=str(i)+"\n"
            print(i)
        return returnStr

    def toAdjacencyList(self):
        return AdjacencyList(super().toAdjacencyList())
    def toAdjacencyMatrix(self):
        return AdjacencyMatrix(super().toAdjacencyMatrix())
    def toIncidentMatrix(self):
        return self