def sort(sortArray):
    swaps = 0
    for i in range(1, len(sortArray)):
        k = i
        while k > 0 and sortArray[k] < sortArray[k-1]:
            sortArray[k], sortArray[k-1] = sortArray[k-1], sortArray[k]
            swaps += 1
            k -= 1
    return (swaps, sortArray)

with open(input("Provide file path: "), "r") as f:
    array = []
    count = f.readline()
    items = f.readline().split(" ")
    for item in items:
        array.append(int(item))
    print(sort(array)[0])