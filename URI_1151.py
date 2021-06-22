p = 0
s = 1
fibo = [p,s]
a = int(input())
for i in range(2, a):
    t = s+p
    p = s
    s = t
    fibo.append(t)
print(' '.join(map(str, fibo)))