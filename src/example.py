def BellmanFord(graph, s):
    """
    Applies Bellman-Ford to compute single-source
    shortest paths.
    """
    dst = [float('inf') for v in graph.vertices()]
    pnt = [None for V in graph.vertices()]

    dst[s] = 0
    numRelaxations = graph.numVertices()-1
    for relaxation in range(numRelaxations):
        for (u, v) in graph.edges():
            new_dst = dst[u] + graph.weight[(u,v)]
            if new_dst < dst[v]:
                dst[v] = new_dst
                pnt[v] = u 

    if any(dst[u] + graph.weight[(u,v)] < dst[v] for (u, v) in graph.edges()):
        return (None, None)
    
    return (dst, pnt)


def showResults(graph, dst, pointer):
    """
    Shows all-pairs shortest paths information.
    """
    if dst == None:
        print(None)
        return

    print("Distances:")
    for (v, row) in zip(graph.vertices(), dst):
        print(f"{v}: {row}")

    print("\nPath Pointers:")
    for (v, row) in zip(graph.vertices(), pointer):
        print(f"{v}: {row}")