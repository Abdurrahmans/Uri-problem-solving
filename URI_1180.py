
n = int(input())
arr = list(map(int, input().split()))
p = 0
m = arr[0]
count = 0
for i in arr:
    if i < m:
        m = i
        p = count
    count += 1
print("Menor valor: {}".format(m))
print("Posicao: {}".format(p))
