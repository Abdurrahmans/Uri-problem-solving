
arr = []
for x in range(100):
   arr.append(float(input()))
for x in range(100):
    if arr[x]<=10:
        print ('A[{0}] = {1}'.format(x, arr[x]))