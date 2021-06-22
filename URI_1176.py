
arr = [0,1]
a = 0
t = 1
for i in range(5):
    tnp = t+a
    arr.append(tnp)
    a = t
    t = tnp
n = int(input())
for i in range(n):
    value = int(input())
    print('Fib({0}) = {1}'.format(value, arr[value]))