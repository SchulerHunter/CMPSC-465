import networkx
g = networkx.DiGraph()
distDict = {}

with open(input("Provide file path: "), "r") as f:
    edgeArray = []
    count = int(f.readline().split(" ")[0])
    for node in range(1, count+1):
        g.add_node(node)
        distDict.update({node:-1})
    edges = f.readlines()
    for edge in edges:
        edge = edge.split(" ")
        edgeArray.append((int(edge[0]), int(edge[1])))
    g.add_edges_from(edgeArray)

with open("output.txt", "w") as f:
    q = []
    q.append(1)
    dist = 0
    distDict.update({1:0})
    while q:
        node = q.pop(0)
        dist = distDict[node] + 1
        for neighbor in g.neighbors(node):
            if distDict[neighbor] == -1:
                q.append(neighbor)
                distDict.update({neighbor:dist})
    for key in distDict:
        f.write(str(distDict[key])+" ")