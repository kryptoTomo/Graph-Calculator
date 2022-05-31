import random
from sklearn.utils import shuffle
from collections import defaultdict
import Utils
import math

def charToIntConvert(c):
    return ord(c) - ord('a') + 1


#ex1
def random_flow_network(n):
    if 2 <= n <= 4:

        layers = []
        layers.append(["S"])  # layer #0 -> source 'S'
        idNode = 'a'

        for i in range(n):
            layer = []

            for _ in range( random.randint(2,n) ):
                layer.append(idNode)
                idNode = chr(ord(idNode) + 1) # increment node 'name'
            layers.append(layer)

        layers.append(["T"])    # layer N+1 => target 'T'

        amount_of_nodes = 0
        for layer in layers:
            amount_of_nodes += len(layer)

        adj_matrix = [[0 for x in range(amount_of_nodes)] for y in range(amount_of_nodes)] #adjacency matrix

        #edges from source
        for i in range(len(layers[1])):     #skip 'source' layer
            adj_matrix[0][charToIntConvert(layers[1][i])] = random.randint(1,10)

        for i in range(1, n):

            iLayer = layers[i]
            iLayer_id = []
            for node in iLayer:
                iLayer_id.append(charToIntConvert(node))
            
            iLayer_next = layers[i+1]
            iLayer_next_id = []
            for node in iLayer_next:
                iLayer_next_id.append(charToIntConvert(node))

            if(len(iLayer_id) == len(iLayer_next_id)):
                shuffle(iLayer_id)
                shuffle(iLayer_next_id)

                for _ in range(len(iLayer_id)):
                    adj_matrix[ iLayer_id.pop() ][ iLayer_next_id.pop() ] = random.randint(1,10)

            elif len(iLayer_id) > len(iLayer_next_id):
                layer_copy = iLayer_next_id.copy()
                shuffle(iLayer_id)
                shuffle(iLayer_next_id)
                shuffle(layer_copy)

                for _ in range(len(iLayer_next_id)):
                    adj_matrix[ iLayer_id.pop() ][ iLayer_next_id.pop() ] = random.randint(1,10)

                for _ in range(len(iLayer_id)):
                    adj_matrix[ iLayer_id.pop() ][ layer_copy.pop() ] = random.randint(1,10)

            else:
                layer_copy = iLayer_id.copy()
                shuffle(iLayer_id)
                shuffle(iLayer_next_id)
                shuffle(layer_copy)

                for _ in range(len(iLayer_id)):
                    adj_matrix[ iLayer_id.pop() ][ iLayer_next_id.pop() ] = random.randint(1,10)

                for _ in range(len(iLayer_next_id)):
                    adj_matrix[ layer_copy.pop() ][ iLayer_next_id.pop() ] = random.randint(1,10)
        
        #edges to 'T'
        for i in range(len(layers[n])):
            adj_matrix[ charToIntConvert(layers[n][i]) ][amount_of_nodes-1] = random.randint(1,10)

        # 2N add
        edges = 0
        while edges < (2*n):
            x = random.randint(1, amount_of_nodes-2)
            y = random.randint(1, amount_of_nodes-2)

            if x!=y and adj_matrix[x][y] == 0 and adj_matrix[y][x] == 0:
                adj_matrix[x][y] = random.randint(1,10)
                edges += 1
        
        return adj_matrix, layers
    else:
        print("Zla ilosc warstw posrednich!")
        return None, None

def convert(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]!= 0:
                adjList[i].append(j)
    return adjList


# g, layers = random_flow_network(3)
# Utils.plot_graph(g, layers, filename='1')
# print(layers)

########################################################################################################
#ex2
def BFS(G, s):
    t = len(G) - 1
    if s>=len(G) or s<0:
        print("Zly poczatkowy wierzcholek")
    if t >=len(G) or t<0:
        print("Zly koncowy wierzcholek")
        
    d = [math.inf for _ in range(len(G))]
    p = [None for _ in range(len(G))]
    d[s] = 0
    Q=[]
    Q.append(s)

    while len(Q)>0 and d[t] == math.inf:
        v = Q.pop(0)
        for u in range(len(G)):
            if G[v][u] != 0 and d[u]==math.inf:
                d[u] = d[v] + 1
                p[u] = v
                Q.append(u)
    return d, p

def cap_residual(u, v, G, c, f):    # residual 'bandwidth' between u-> v
    if G[u][v] != 0:
        return c[(u, v)] - f[(u, v)]
    if G[v][u] != 0:
        return f[(v, u)]
    return 0

def Ford_Fulkerson(G):
    if G is None:
        return None, None
    # G -> adj matrix
    s = 0
    f = {}  #flow
    c = {}  #bandwidth

    for u in range(len(G)):
        for v in range(len(G)):
            if G[u][v] != 0:
                f[(u, v)] = 0   
                c[(u, v)] = G[u][v] 

    G_res = [[cap_residual(u, v, G, c, f) for v in range(len(G))] for u in range(len(G))]
    (d, p) = BFS(G_res, s)

    t = len(G)-1    # target 'T'  (last layer)
    while d[t] != math.inf:
        extPath = []
        v = t

        while v!=None and p[v]!=None:
            extPath.append( (p[v],v) )
            v = p[v]
        extPath.reverse()

        res_p = math.inf
        for i in range(len(extPath)):
            u = extPath[i][0]
            v = extPath[i][1]
            res_p = min( cap_residual(u, v, G, c, f), res_p)

        for i in range(len(extPath)):
            u = extPath[i][0]
            v = extPath[i][1]
            if G[u][v] != 0:
                f[(u, v)] += res_p
            else:
                f[(v, u)] -= res_p

        G_res = [ [cap_residual(u, v, G, c, f) for v in range(len(G))] for u in range(len(G)) ]
        # print(G_res)
        (d, p) = BFS(G_res, s)

    fmax=0
    keys=list(f.keys())
    values= list(f.values())
    for i in range(len(f)):
        if 0 in keys[i]:
            fmax += values[i]
    return f, fmax

# g, layers = random_flow_network(3)
# print(layers)
# f, fmax = Ford_Fulkerson_Ziom(g)
# print(f"Wartosc maksymalnego przeplywu |Fmax| = {fmax}")
# Utils.plot_graph(g, layers, filename='2', flow=f)