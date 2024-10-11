def makeGraph(n_vertices):
    adjacencias = {i: [] for i in range(n_vertices)}

    for i in range(n_vertices):
        if i == 0:
            adjacencias[i].extend([1, 2])
        elif i == 1:
            adjacencias[i].extend([0, 2])
        elif i == n_vertices - 2:
            adjacencias[i].extend([i - 1, i + 1])
        elif i == n_vertices - 1:
            adjacencias[i].extend([i - 1, i - 2])
        else:
            if i % 2 == 0:
                adjacencias[i].extend([i - 2, i - 1, i + 1, i + 2])
            else:
                adjacencias[i].extend([i - 1, i + 1])

    return adjacencias