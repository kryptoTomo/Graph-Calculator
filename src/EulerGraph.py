import random as rnd
from Representation import AdjacencyList
from Utils import valid_graph, cons_graph
from random import choice
from Representation import *
from copy import deepcopy

class EulerGraph():
    def __init__(self,nodes):
        self.nodes = nodes
        self.graph = cons_graph(self.generate_random_euler_graph(self.nodes)).toAdjacencyList()
        self.graph.graphVisualization()
        self.graphList =  deepcopy(list(self.graph.graph.values()))
        self.euler_cycle = []
        current = 0
        for i in range(self.nodes):
            if len(self.graphList[i]) %2 != 0 :
                current = i
                break
        self.create_euler_tour(current)
        self.graphList =  deepcopy(list(self.graph.graph.values()))
        self.euler_cycle = self.euler_cycle[0:len(self.euler_cycle)//2+1]

    def generate_random_euler_graph(self,nodes):
        if nodes <= 2:
            raise ValueError("Invalid number of nodes provided")
        even_numbers_form_the_n = [i for i in range(2, nodes, 2)]
        graphic_seq = []
        while not (valid_graph(graphic_seq)):
            graphic_seq = []
            for _ in range(self.nodes):
                graphic_seq.append(choice(even_numbers_form_the_n))
        return graphic_seq
    
    def create_euler_tour(self,current):
        for node in self.graphList[current]:
            if self.checkNextEdge(current, node):
                last=node
                self.euler_cycle.append(current)
                self.removeEdge(current, node)
                self.create_euler_tour(node)
        self.euler_cycle.append(current)

    def removeEdge(self, current, node):
        for index, key in enumerate(self.graphList[current]):
            if key == node:
                self.graphList[current].pop(index)
        for index, key in enumerate(self.graphList[node]):
            if key == current:
                self.graphList[node].pop(index)

    def count_how_many_nodes_can_i_get_to(self, node, visited):
        count = 1
        visited[node] = True
        for i in self.graphList[node]:
            if visited[i] == False:
                count = count + self.count_how_many_nodes_can_i_get_to(i, visited)        
        return count
 
    def checkNextEdge(self, current, node):
        if len(self.graphList[current]) == 1:
            return True
        else:  
            visited =[False]*(self.nodes)
            count1 = self.count_how_many_nodes_can_i_get_to(current, visited)
            self.removeEdge(current, node)
            visited =[False]*(self.nodes)
            count2 = self.count_how_many_nodes_can_i_get_to(current, visited)
            self.graphList[current].append(node)
            self.graphList[node].append(current)
            return False if count1 > count2 else True
 
    def __str__(self):
        tmp="["
        tmp+=''.join(f'{k} - ' for k in self.euler_cycle)
        print(len(self.euler_cycle))
        return tmp[:-3]+']'

