def heapify(arr, i):
    largest = i
    l = 2*i+1
    r = (i+1)*2
    if l < len(arr) and arr[l] > arr[largest]:
        largest = l
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest)

def buildHeap(arr):
    start = len(arr)//2-1
    for i in range(start, -1, -1):
        heapify(arr, i)  


values = []
with open(input("Provide file path: "), "r") as f:
    size = f.readline()
    values = f.readline().split(" ")
    for i in range(len(values)):
        values[i] = int(values[i])
    buildHeap(values)

with open("output.txt", "w") as f:
    for val in values:
        f.write(str(val) + " ")