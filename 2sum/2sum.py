def findOpp(arr):
    tempArr = []
    for val in arr:
        if -val in tempArr:
            if val != 0:
                return (min(arr.index(val), arr.index(-val)), max(arr.index(val), arr.index(-val)))
            # If 0, return second 0 through enumerate
            return (arr.index(val), [i for i, n in enumerate(arr) if n == val][1])
        tempArr.append(val)
    return (0, 0, 0)


arrays = []
count = 0
with open(input("Provide file path: "), "r") as f:
    count = int(f.readline().split(" ")[1])
    tempArrays = f.readlines()
    for array in tempArrays:
        array = array.split(" ")
        for i in range(len(array)):
            array[i] = int(array[i])
        arrays.append(array)

with open("output.txt", "w") as f:
    for array in arrays:
        result = findOpp(array)
        if result[0] == result[1]:
            f.write("-1\n")
        else:
            f.write(str(result[0]+1)+" "+str(result[1]+1)+"\n")