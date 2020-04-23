def find3(arr):
    tArr = arr.copy()
    tArr.sort()
    for i in range(len(arr)-2):
        a = tArr[i]
        s = i + 1
        e = len(arr) - 1
        while (s < e):
            b = tArr[s]
            c = tArr[e]
            if a + b + c == 0:
                return [a, b, c]
            elif a + b + c > 0:
                e -= 1
            else:
                s += 1
    return [0, 0, 0]

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
        result = find3(array)
        if result[0] == result[1]:
            f.write("-1\n")
        else:
            for i in range(len(result)):
                result[i] = array.index(result[i])+1
            result.sort()
            f.write(str(result[0])+" "+str(result[1])+" "+str(result[2])+"\n")