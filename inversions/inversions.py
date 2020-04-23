def getInversions(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i] > arr[j]):
                count += 1
    return count

with open(input("Provide file path: "), "r") as f:
    arrSize = int(f.readline())
    values = f.readline().split(" ")
    for i in range(len(values)):
        values[i] = int(values[i])
    print(getInversions(values, arrSize))