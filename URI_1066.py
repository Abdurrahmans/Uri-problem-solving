count = 0
count1 = 0
count2 = 0
count3 = 0
for x in range(5):
    value = int(input())
    if value%2==0:
      count +=1
    if value % 2 == 1:
        count1 += 1
    if value >0:
        count2 += 1
    if value<0:
        count3 += 1
print('{} valor(es) par(es)'.format(count))
print('{} valor(es) impar(es)'.format(count1))
print('{} valor(es) positivo(s)'.format(count2))
print('{} valor(es) negativo(s)'.format(count3))
