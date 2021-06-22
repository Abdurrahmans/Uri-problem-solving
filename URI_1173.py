arr = [0,0,0,0,0,0,0,0,0,0]
v = int(input())
if v < 50:
    for x in range(len(arr)):
        arr[x] = v
        v = v * 2
        print('N[{0}] = {1}'.format(x, arr[x]))
