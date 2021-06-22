n = input()
arr = []
for i in range(12):
    for j in range(12):
        value = float(input())
        if i > j:
            arr.append(value)

if n == "S":
    print('{:.1f}'.format(sum(arr)))
else:
    print('{:.1f}'.format(sum(arr) / len(arr)))
