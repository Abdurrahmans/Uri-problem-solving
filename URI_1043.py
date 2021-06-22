A,B,C = map(float,input().split())
perimeter = A+B+C
area = ((A+B)/2)*C
if (A+B)>C and (B+C)>A and (A+C)>B:
    print('Perimetro = {:.1f}'.format(perimeter))
else:
    print('Area = {:.1f}'.format(area))