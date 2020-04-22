def quickSort(numList):
    n=len(numList)
    if n<=1:
        return numList
    # Set pivot to end of list and reassign right to before the pivot
    x, left, right = numList[n-1], 0, n-2
    # Loop until left is greater than pivot
    while left<=right:
        if numList[left]<=x:
            left+=1
        else:
            # Check if left is greater than pivot, then if right is less than pivot
            if numList[right]<=x:
                numList[left], numList[right] = numList[right], numList[left]
            right -=1
    numList[left], numList[n-1] = numList[n-1], numList[left]
    # Recursively reassign the list values
    numList[:left] = quickSort(numList[:left])
    numList[left+1:] = quickSort(numList[left+1:])
    return numList

values = []
with open(input("Provide file path: "), "r") as f:
    size = int(f.readline())
    values = f.readline().split(" ")
    for i in range(len(values)):
        values[i] = int(values[i])
    values = quickSort(values)

with open("output.txt", "w") as f:
    for val in values:
        f.write(str(val)+" ")
    