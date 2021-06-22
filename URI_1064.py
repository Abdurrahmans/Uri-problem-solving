
count = 0
sum=0
for x in range(6):
    value =float(input())
    if value>0:
      sum +=value
      count +=1
      avg = sum/count
print('{} valores positivos'.format(count))
print('{:.1f}'.format(avg))