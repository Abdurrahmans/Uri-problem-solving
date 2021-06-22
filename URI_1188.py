n = input()
sum = 0
count = 0
for i in range(12):
    for j in range(12):
        value = float(input())
        if 12 <= i + j and i >= 7 and i >j:
            sum = sum + value
            count = count + 1
if n == "S":
    print('{:.1f}'.format(sum))
else:
    print('{:.1f}'.format(sum/count))


