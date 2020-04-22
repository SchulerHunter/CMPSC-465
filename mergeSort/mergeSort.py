def merge(list1, list2):
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    if i < len(list1):
        for k in range(len(list1[i:])):
            result.append(list1[k+i])
    else:
        for k in range(len(list2[j:])):
            result.append(list2[k+j])
    return result

def mergeSort(numList):
    if len(numList) < 2:
        return numList
    middle = len(numList) // 2
    leftHalf = mergeSort(numList[:middle])
    rightHalf = mergeSort(numList[middle:])
    return merge(leftHalf, rightHalf)

values = []
with open(input("Provide file path: "), "r") as f:
    size = f.readline()
    values = f.readline().split(" ")
    for i in range(len(values)):
        values[i] = int(values[i])
    values = mergeSort(values)

with open("output.txt", "w") as f:
    for val in values:
        f.write(str(val)+" ")