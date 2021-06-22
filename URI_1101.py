sum = 0
j=0
while j != 1:
    a,b = map(int,input().split( ))
    sum = 0
    if a > b:
        c = a
        a = b
        b = c
    if a <= 0 or b <= 0:
        j = 1
    if j != 1:
        for i in range(a,b+1):
            print('{}'.format(i))
            sum +=i
            if i == b:
                print('Sum={}'.format(sum))