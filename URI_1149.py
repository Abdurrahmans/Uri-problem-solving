num = input()
list = num.split()
temp = []
soma = []

cont = 0

for i in list:
    if i > "0":
        temp.append(i)
        if len(temp) == 2:
            break

x = int(temp[0])
y = int(temp[1])

while cont < y:
    soma.append(x)
    x = x + 1
    cont += 1

print(sum(soma))


