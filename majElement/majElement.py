def majElement(array, count):
    val = max(array,key=array.count)
    if (array.count(val) > count/2):
        return val
    return -1

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
        f.write(str(majElement(array, count)) + " ")
