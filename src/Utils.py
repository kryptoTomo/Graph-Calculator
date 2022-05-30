from collections import defaultdict
from Representation import AdjacencyList, AdjacencyMatrix, example_data, dijkstra_data
import copy
import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

#------------------------------------------------------------------------------------------------------------------
#
# PROJECT 2
#
#------------------------------------------------------------------------------------------------------------------
#ex1
def valid_graph(seq):
    if len(seq)==0:
        return False
    # jeśli liczba wszystkich nieparzystych elementów jest nieparzysta, to ciąg na pewno nie jest graficzny
    seq = sorted(seq, reverse=True)
    if sum(1 for i in seq if i%2==1)%2 == 1:
        return False
    while True:
        if all(i==0 for i in seq):
            return True #Jeśli tablica składa się z samych zer, to ciąg wejściowy jest graficzny
        if seq[0]<0 or seq[0]>=len(seq) or any(i<0 for i in seq):
            return False
        for i in range(1, seq[0]+1):
            seq[i] = seq[i]-1
        seq[0] =0
        seq = sorted(seq, reverse=True)

#ex2   
def randomizeGraph(adjacency_list,numberOfRandomize): 
    i=0
    data={'name': 'RandomizeGraph.png','size': (6, 6),'directed_all': False,'node_size': 500,'graph': copy.deepcopy(adjacency_list.graph),'nodes_description':{},'edges_description':{}}
    while i<numberOfRandomize:
        a=random.sample(list(data['graph'].keys()),1)[0]
        b=random.sample(list(data['graph'][a]),1)[0]
        c=random.sample(list(data['graph'].keys()),1)[0]
        d=random.sample(list(data['graph'][c]),1)[0]
        if a!=c and a!=d and b!=c and b!=d and c not in data['graph'][a] and d not in data['graph'][b]:
            data['graph'][a].remove(b)
            data['graph'][b].remove(a)

            data['graph'][c].remove(d)
            data['graph'][d].remove(c)

            data['graph'][a].append(c)
            data['graph'][c].append(a)

            data['graph'][b].append(d)
            data['graph'][d].append(b) 

            i+=1
    return AdjacencyList(data)

#konstrukcja grafu prostego  o stopniach wierzchołków zadanych przez ciąg graficzny
def cons_graph(seq):
    seq = sorted(seq, reverse=True)
    out = []
    
    data={'name': 'CoherentComponent.png','size': (6, 6),'directed_all': False,'node_size': 500,'graph': {},'nodes_description':{},'edges_description':{}}
    for i in range(len(seq)):                       #+1
        data['graph'][i]=[]

    verts = [[i, seq[i]] for i in range(len(seq))]  #+1
    for i in range(len(seq)):
        for j in range(1, 1 + verts[0][1]):
            out.append([verts[0][0], verts[j][0]])
            verts[j][1] -= 1
        verts[0][1] = 0
        verts.sort(key=lambda x: x[1], reverse=True)
    out.sort()

    for i in range(len(out)):
        data['graph'][out[i][0]].append(out[i][1])
        data['graph'][out[i][1]].append(out[i][0])
    #data['graph'].pop(0)
    return AdjacencyList(data)

#znajdowanie najwiekszej spojnej skladowej
#ex3
def components_rec(nr, v, G, comp):
    for u in G[v]:
        if comp[u] == -1:
            comp[u] = nr
            components_rec(nr,u,G,comp)

def components(G):
    nr=0
    comp = [-1] * len(G.keys())

    for v in G.keys():
        if comp[v] == -1:
            nr += 1
            comp[v] = nr
            components_rec(nr, v, G, comp)

    comp_repr = defaultdict(list)

    for i,k in enumerate(comp):
        comp_repr[k].append(i)  #i+1

    comp_big=0
    comp_big_len=0
    comps=[]
    tmpStr=""
    for comp, comp_v in sorted(comp_repr.items()):
        if len(comp_v) > comp_big_len:
            comp_big = comp
            comp_big_len = len(comp_v)
        tmpStr+=f'{comp}) {[i+1 for i in comp_v]}\n'
        print(f'{comp}) {comp_v}')
        comps.append(comp_v)

    print(f"Najwieksza skladowa ma numer {comp_big}.")
    tmpStr+=f"Najwieksza skladowa ma numer {comp_big}.\n"
    return tmpStr
    # return comps, comp_big

#ex5
#generowanie losowych grafów k-regularnych 
#n - ilosc wierzcholkow
def random_k_regular(k,n):
    if n-k>0:
        seq = [k for _ in range(n)]
        randomizeGraph(cons_graph(seq),100).graphVisualization()

#poszukiwania cyklu Hamiltona
#ex6
def find_Hamiltion_cycle(graph, v=1, stack=[]):
    if v not in stack:
        stack.append(v)

        if len(graph) == len(stack):
            if stack[-1] in graph[stack[0]]:
                stack.append(stack[0])
                return [x for x in stack]
            else:
                stack.pop()
                return None
        
        for x in graph[v]:
            tmp_stack = copy.deepcopy(stack)
            res = find_Hamiltion_cycle(graph, x, tmp_stack)
            if res is not None:
                return res

#------------------------------------------------------------------------------------------------------------------
#
# PROJECT 3
#
#------------------------------------------------------------------------------------------------------------------

#ex2
def dijkstraWeight(data):
    weight_matrix = []
    for node in data.graph:
        x = []
        for path in range(len(data.graph)):
            if path == node:
                x.append(0)
            elif (node, path) in data.edges_description:
                x.append(data.edges_description[(node,path)]['weight'])
            elif (path, node) in data.edges_description:
                x.append(data.edges_description[(path,node)]['weight'])
            else:
                x.append(0)
        weight_matrix.append(x)
    print("graph: ",data.graph)    
    print("edges: ",data.edges_description)
    print('weight_matrix: ', weight_matrix)
    return weight_matrix

def dijkstraMinDistance(weights, used):
        min = 1e10
        for weight in range(len(weights)):
            if weights[weight] < min and used[weight] == False:
                min = weights[weight]
                min_index = weight
        return min_index

def dijkstra(source, data):
        if source >= len(data.graph):
            return
        weight_matrix = dijkstraWeight(data)
        currentWeights = [1e10 for _ in range(len(data.graph))]
        currentWeights[source] = 0
        used = [False for _ in range(len(data.graph))]
 
        for _ in range(len(data.graph)):
            min = dijkstraMinDistance(currentWeights, used)
            used[min] = True
            for v in range(len(data.graph)):
                if (weight_matrix[min][v] > 0 and used[v] == False and currentWeights[v] > currentWeights[min] + weight_matrix[min][v]):
                    currentWeights[v] = currentWeights[min] + weight_matrix[min][v]
        return currentWeights

#ex3
def dijkstraDist(data = dijkstra_data):
    matrix = []
    for i in range(len(data.graph)):
        matrix.append(dijkstra(i+1, data))
    print(matrix)
    return matrix

#ex4
def graphCenter(data = dijkstra_data):
    matrix = dijkstraDist(data)
    l = []
    for m in matrix:
        l.append(sum(m))
    center = l.index(min(l)) + 1
    print(center)

def miniMaxCenter(data = dijkstra_data):
    matrix = dijkstraDist(data)
    l = []
    for m in matrix:
        l.append(max(m))
    minimax = l.index(min(l)) + 1
    print(minimax)

#ex5
def prim(data = dijkstra_data):
    weights = dijkstraWeight(data)
    key = [1e10 for _ in range(len(data['graph']))]
    MST = [0 for _ in range(len(data['graph']))]
    key[0] = 0
    used = [False for _ in range(len(data['graph']))]
    MST[0] = -1

    for _ in range(len(data['graph'])):
        min_dist = 1e10
        for node in range(len(data['graph'])):
            if key[node] < min_dist and used[node] == False:
                min_dist = key[node]
                min = node   
        used[min] = True
        for v in range(len(data['graph'])):
                if weights[min][v] > 0 and used[v] == False and key[v] > weights[min][v]:
                        key[v] = weights[min][v]
                        MST[v] = min
    print(MST)
    for i in range(1, len(data['graph'])):
            print (MST[i] + 1, "-", i + 1, "\t", weights[i][MST[i]])


#------------------------------------------------------------------------------------------------------------------
#
# PROJECT 5
#
#------------------------------------------------------------------------------------------------------------------

def plot_graph(matrix, layers, filename, flow=None):
    if matrix is None:
        return

    plt.figure(figsize=(6,6))

    edges = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                edges.append((i+1, j+1, matrix[i][j])) 

    colors = []
    for k in range(len(edges)):
        if flow!=None and  flow[( edges[k][0]-1, edges[k][1]-1 )] != 0:
            colors.append('#0ee6d4')
        else:
            colors.append('#000000')

    G = nx.DiGraph()
    G.add_nodes_from(list( range(1, len(matrix)+1) ))

    edgesL = []
    for i in range(len(edges)):
        if edges[i][0] == edges[i][1]:
            edgesL.append(edges[i])
        else:
            G.add_edge(edges[i][0], edges[i][1], weight=edges[i][2])

    labels = {}
    pos = {}
    nodes = np.concatenate(layers)
    x = 0
    for i in range(len(layers)):
        for v in range(len(layers[i])):
            x += 1
            # pos.update({(x): (i*10+ 5*v, v * 20)})        # polozenia wierzcholkow nie na okregu 
            labels[x] = nodes[x-1]

    pos = nx.circular_layout(G)
    nx.draw(G,pos,labels=labels, arrows=True, node_size=500, node_color='#0eafd4', edge_color=colors)

    for i in range(len(edgesL)):
        G.add_edge(edgesL[i][0], edgesL[i][1], weight=edgesL[i][2])
    nx.draw_networkx_edges(G, pos, edgelist=edgesL)

    l = nx.get_edge_attributes(G, 'weight')
    labels = {}
    for key, value in l.items():
        labels[(key[0], key[1])] = str(flow[(key[0]-1, key[1]-1)]) + "/" + str(value) if flow!=None else value

    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10, label_pos = 0.15)
    plt.savefig(f'src/__imgcache__/{filename}')
    plt.close()
