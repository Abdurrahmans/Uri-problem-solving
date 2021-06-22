number = int(input())
sum1=0
sum2=0
for x in range(number):
    value = int(input())
    if (value>=10 and value<=20):
        sum1 +=1
    else:
        sum2 +=1
print('{} in'.format(sum1))
print('{} out'.format(sum2))
