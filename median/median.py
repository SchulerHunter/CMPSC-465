import heapq

values = []
returnNum = 0
with open(input("Provide file path: "), "r") as f:
    arrSize = int(f.readline())
    values = f.readline().split(" ")
    for i in range(len(values)):
        values[i] = int(values[i])
    returnNum = int(f.readline())
    heapq.heapify(values)
    for i in range(returnNum):
        if i == returnNum - 1:
            print(heapq.heappop(values))
        else:
            heapq.heappop(values)
