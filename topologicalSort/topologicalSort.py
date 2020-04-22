import networkx as nx
g = nx.DiGraph()

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
    for node in list(nx.topological_sort(g)):
        f.write(str(node)+" ")