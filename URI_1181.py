l = int(input())
opera = input()

arr = []
for i in range(12):
    arr.append([])

for i in range(12):
    for j in range(12):
        x = float(input())
        arr[i].append(x)

if opera == 'S':
    sum = 0
    for k in arr[l]:
        sum = sum + k
    print(sum)
if opera == 'M':
    med = 0
    sum = 0
    for k in arr[l]:
        sum = sum + k
    med = sum / 12
    print(med)