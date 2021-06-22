import math
a,b,c = map(float,input().split())
root1 = (b**2)-(4*a*c)
if root1 < 0 or a == 0:
    print('Impossivel calcular')
else:
    R = math.sqrt(root1)
    R1 = (-b+R)/(2*a)
    R2 = (-b-R)/(2*a)
    print('R1 = {:.5f}'.format(R1))
    print('R2 = {:.5f}'.format(R2))

