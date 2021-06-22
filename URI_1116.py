n = int(input())
for x in range(n):
    a,b = map(int,input().split())
    if (a>0 or a<0) and b==0:
        print('divisao impossivel')
        continue
    divisor = a/b
    print(divisor)