n = input()
sum = 0
count = 0
for i in range(12):
    for j in range(12):
        value = float(input())
        if i + j >= 12:
            sum += value
            count = count + 1

if n == "S":
    print('{:.1f}'.format(sum))
else:
    print('{:.1f}'.format(sum/count))
