
arr = []
for x in range(10):
    value = int(input())
    arr.append(value)
    if arr[x] <= 0:
        arr[x] = 1
    else:
        arr[x] = value
    print ('X[{0}] = {1}'.format(x, arr[x]))

