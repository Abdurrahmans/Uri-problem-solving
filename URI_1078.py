x = int(input())
if x>1 and x<1000:
    for i in range(1,11):
        print('{0} x {1} = {2}'.format(i,x,i*x))