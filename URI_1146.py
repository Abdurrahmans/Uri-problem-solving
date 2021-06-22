
while True:
    a = int(input())
    b = ''
    if a == 0:
        break
    for i in range(1, a+1):
        b += str(i) + " "
    print(b[:-1])