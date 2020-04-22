import networkx
g = networkx.Graph()
with open(input("Provide file path: "), "r") as f:
    edgeArray = []
    f.readline() # First line is trash in this case. Only contains nodes and number of edges
    edges = f.readlines()
    for edge in edges:
        edge = edge.split(" ")
        edgeArray.append((int(edge[0]), int(edge[1])))
    g.add_edges_from(edgeArray)

with open("output.txt", "w") as f:
    for node, val in sorted(g.degree(), key=lambda pair: pair[0]):
        f.write(str(val)+" ")