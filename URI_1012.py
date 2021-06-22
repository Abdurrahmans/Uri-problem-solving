A,B,C = input().split(' ')
pi = 3.14159
triangle = (1/2)*(float(A)*float(C))
area =pi*(float(C)* float(C))
square = float(B)*float(B)
rectangle = float(A)*float(B)
trapezium =((float(A)+float(B))/2 *(float(C)))
print('TRIANGULO: {:.3f}'.format(triangle))
print('CIRCULO: {:.3f}'.format(area))
print('TRAPEZIO: {:.3f}'.format(trapezium))
print('QUADRADO: {:.3f}'.format(square))
print('RETANGULO: {:.3f}'.format(rectangle))


