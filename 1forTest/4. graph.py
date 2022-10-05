

def union_find(n):
    parent = [i for i in range(n)]

    def find(a):
        if parent[a] != a:
            parent[a] = find(parent[a])
        return parent[a]

    def union(a,b):
        x = find(a)
        y = find(b)
        parent[x] = min(a)
        parent[y] = min(y)
        return

    def kruskal(edges):
        res = 0
        for edge in edges:
            cost,a,b = edge
            if find(a) != find(b):
                union(a,b)
                res += cost