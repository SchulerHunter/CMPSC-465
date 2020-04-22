def binSearch(key, left, right):
    if right >= left:
        mid = left + (right - left)//2
        if sortList[mid] == key:
            # Element found in middle
            return mid
        elif sortList[mid] > key:
            # Search left half
            return binSearch(key, left, mid-1)
        else:
            # Search right half
            return binSearch(key, mid+1, right)
    else:
        return -2

# Main code
sortList = []
keyList = []
with open(input("Provide file path: "), "r") as f:
    sortSize = int(f.readline())
    keySize = int(f.readline())
    sortListTemp = f.readline().split(" ")
    for val in sortListTemp:
        sortList.append(int(val))
    keyListTemp = f.readline().split(" ")
    for val in keyListTemp:
        keyList.append(int(val))

with open("output.txt", "w") as f:
    for key in keyList:
        f.write(str(binSearch(key, 0, sortSize)+1)+" ")