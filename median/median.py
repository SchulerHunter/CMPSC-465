def sort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
                arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

with open(input("Provide file path: "), "r") as f:
    size = int(f.readline())
    values = f.readline().split(" ")
    for i in range(len(values)):
        values[i] = int(values[i])
    print(sort(values))#[int(f.readline())-1])
