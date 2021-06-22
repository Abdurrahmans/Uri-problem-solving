a = int(input())
b = int(input())
if a > b:
    temp = a
    a = b
    b = temp
    a = a+1
for x in range(a,b):
    if x%5==2 or x%5==3:
        print(x)


