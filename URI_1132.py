a = int(input())
b = int(input())
temp = 0
sum = 0
if a > b:
    temp = b
    b = a
    a = temp
for x in range(a,b):
    if x % 13 != 0:
        sum += x
print(sum)
