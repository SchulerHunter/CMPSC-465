def mergeSorted(arrA, arrB):
    outArr = []
    i, j= 0, 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            outArr.append(arrA[i])
            i += 1
        else:
            outArr.append(arrB[j])
            j += 1
    while i < len(arrA):
        outArr.append(arrA[i])
        i += 1
    while j < len(arrB):
        outArr.append(arrB[j])
        j += 1
    return outArr

output = []
with open(input("Provide file path: "), "r") as f:
    countA = int(f.readline())
    arrayA = f.readline().split(" ")
    for i in range(len(arrayA)):
        arrayA[i] = int(arrayA[i])
    
    countB = int(f.readline())
    arrayB = f.readline().split(" ")
    for i in range(len(arrayB)):
        arrayB[i] = int(arrayB[i])
    output = mergeSorted(arrayA, arrayB)

with open("output.txt", "w") as f:
    for val in output:
        f.write(str(val)+" ")