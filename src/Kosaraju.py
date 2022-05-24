from copy import deepcopy
from Generator import *
from Representation import *
from collections import defaultdict

class Kosaraju:

    def __init__(self, vertex,prob=0, head=False):
        self.V = vertex
        self.graph = defaultdict(list)
        self.result=[]
        self.repres = None
        if head : self.create_graph(Generator.rand_digraph_edge_probability(self.V, prob).toAdjacencyList())

    def add_edge(self, s, d):
        self.graph[s].append(d)

    def create_graph(self,representation):
        self.repres = representation
        representation.graphVisualization()
        # print(representation.graph)
        self.graph=deepcopy(representation.graph)
        # print(self.graph)
        self.V=len(representation.graph.keys())
        self.find_strongly_connected_components()

    def dfs(self, d, visited_vertex,tmp):
        visited_vertex[d] = True
        tmp.append(d)
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex,tmp)
        return tmp

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)


    def find_strongly_connected_components(self):
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = Kosaraju(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                gr.add_edge(j, i)
        
        visited_vertex = [False] * (self.V)

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                tmp=[]
                gr.dfs(i, visited_vertex,tmp)
                self.result.append(tmp)

        # print(self.result)

    def __str__(self):
        return f'{self.result}'
    
    def get_result(self):
        return [self.result, self.repres]
# g = Kosaraju(6,0.2,True)