def hierholzer(graph, start_vertex):
    degree = {vertex: len(neighbors) for vertex, neighbors in graph.items()}
    stack = [start_vertex]
    cycle = []

    while stack:
        u = stack[-1]
        if degree[u] > 0:
            v = graph[u].pop()
            graph[v].remove(u)
            degree[u] -= 1
            degree[v] -= 1
            stack.append(v)
        else:
            cycle.append(stack.pop())

    return cycle[::-1]