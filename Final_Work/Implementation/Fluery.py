def eh_ponte(G, u, v):
    G[u].remove(v)
    G[v].remove(u)

    visitados = [False] * len(G)

    def dfs(v):
        visitados[v] = True
        for w in G[v]:
            if not visitados[w]:
                dfs(w)

    dfs(u)

    G[u].append(v)
    G[v].append(u)

    return not visitados[v]

def fleury(G, u):
    arestas = sum(len(v) for v in G.values()) // 2

    C = [u]

    while arestas > 0:
        for v in G[u][:]:
            if len(G[u]) > 1 and eh_ponte(G, u, v):
                continue

            G[u].remove(v)
            G[v].remove(u)

            C.append(v)
            u = v
            arestas -= 1
            break
    return C


