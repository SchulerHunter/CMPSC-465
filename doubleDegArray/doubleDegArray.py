import networkx
g = networkx.Graph()

with open(input("Provide file path: "), "r") as f:
    edgeArray = []
    count = int(f.readline().split(" ")[0])
    for node in range(1, count+1):
        g.add_node(node)
    edges = f.readlines()
    for edge in edges:
        edge = edge.split(" ")
        edgeArray.append((int(edge[0]), int(edge[1])))
    g.add_edges_from(edgeArray)

with open("output.txt", "w") as f:
    for node, val in sorted(g.degree(), key=lambda pair: pair[0]):
        totEdges = 0
        for n in g[node]:
            totEdges += g.degree[n]
        f.write(str(totEdges)+" ")