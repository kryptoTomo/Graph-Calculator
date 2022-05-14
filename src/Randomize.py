import random
import copy
from Representation import AdjacencyList,data2

def randomizeGraph(adjacency_list,numberOfRandomize): 
    i=0
    data={'name': 'Ad.png',
           'directed': True,
           'colors': [],
           'graph': copy.deepcopy(adjacency_list.graph)
           }
    while i<numberOfRandomize:
        a=random.sample(list(data['graph'].keys()),1)[0]
        b=random.sample(list(data['graph'][a]),1)[0]
        c=random.sample(list(data['graph'].keys()),1)[0]
        d=random.sample(list(data['graph'][c]),1)[0]
        if a!=c and a!=d and b!=c and b!=d and c not in data['graph'][a] and d not in data['graph'][b]:
            print('a={},b={},c={},d={}'.format(a,b,c,d))
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
# randomizeGraph(AdjacencyList(data2),0).graphVisualization()