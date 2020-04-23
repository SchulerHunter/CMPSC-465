def part(arr, val):
    lo = []
    eq = []
    hi = []
    for i in range(len(arr)):
        if arr[i] < val:
            lo.append(arr[i])
        elif arr[i] == val:
            eq.append(arr[i])
        else:
            hi.append(arr[i])
    return lo+eq+hi

values = []
with open(input("Provide file path: "), "r") as f:
    arrSize = int(f.readline())
    values = f.readline().split(" ")
    for i in range(len(values)):
        values[i] = int(values[i])

with open("output.txt", "w") as f:
    for val in part(values, values[0]):
        f.write(str(val)+" ")