length = []
n = int(input())
if n<10000:
    for x in range(n):
        length.append(int(input()))
    for value in length:
        if value%2 !=0 and value<0:
            print('ODD NEGATIVE')
        elif value==0:
            print('NULL')
        elif value % 2!=0 and value>0:
            print('ODD POSITIVE')
        elif value % 2==0 and value<0:
            print('EVEN NEGATIVE')
        elif value % 2==0 and value>0:
            print('EVEN POSITIVE')