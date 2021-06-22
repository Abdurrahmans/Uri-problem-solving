n = int(input())
for x in range(n):
    a,b,c = map(float,input().split())
    avg = (a*2+b*3+c*5)/(2+3+5)
    print('{:.1f}'.format(avg))