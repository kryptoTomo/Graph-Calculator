

from copy import deepcopy
from Generator import Generator

class ShortPaths:
    @staticmethod
    def bellman_ford(root,graph,vertex):
        
        dist = [float("Inf")] * vertex
        dist[root] = 0
    
        for _ in range(vertex - 1):
            for u, v, w in graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

        for u, v, w in graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle!!!!!")
                return False

        return dist

    @staticmethod
    def dijkstra(s,graph,weight,vertex):
        from include.heap import Min_Heap
        dist = [float('inf') for v in range(vertex)]
        parent = [None for v in range(vertex)]

        queue = Min_Heap()
        queue.insert(0, s)
        # print(graph)
        while queue:
            d, u = queue.extract_min()
            dist[u] = d

            for v in graph[u]:
                new_dist = d + weight[(u, v)]['weight']

                if v not in queue:
                    if new_dist < dist[v]:
                        queue.insert(new_dist, v)
                        parent[v] = u

                elif new_dist < queue.key(v):
                    queue.decrease_key(v, new_dist)
                    parent[v] = u

        return (dist, parent)

    @staticmethod
    def johnson(representation):
        vertex=len(representation.graph)
        edges = deepcopy(representation.edges_description)
        # print(edges)
        graph=[]

        for i in representation.graph.keys():
            for j in representation.graph[i]:
                graph.append([i,j,representation.edges_description[(i,j)]['weight']])

        result = ShortPaths.bellman_ford(vertex-1,graph,vertex)
        if result:
            for u,v in representation.edges_description:
                edges[(u, v)]['weight'] += result[u] - result[v]
        else : return str(False)

        dst = [None for u in range(vertex)]
        nxt = [None for u in range(vertex)]
        graph=deepcopy(representation.toAdjacencyList().graph)
        for u in range(vertex):
            dst[u], nxt[u] = ShortPaths.dijkstra(u,graph,edges,vertex)

        for u in range(vertex):
            for v in range(vertex):
                delta_h = result[u] - result[v]
                dst[u][v] -= delta_h
        res = ''
        for i in range(vertex):
            res+=str(dst[i])+'\n'
        return res

# t=Generator.rand_digraph_edge_probability(6, 0.4).toAdjacencyList()
# t.graphVisualization()
# ShortPaths.johnson(t)


        
