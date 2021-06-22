a = int(input())
b = int(input())
count = 0
if(a % 2 == 0):
  for i in range(a, b, -1):
    if(i % 2 != 0):
      count += i
else:
  a -= 1
  for i in range(a, b, -1):
    if(i % 2 != 0):
      count += i
print(count)