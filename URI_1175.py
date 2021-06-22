
a = []
for i in range(5):
    value = int(input())
    a.append(value)
pos = 0
for l in a[::-1]:
    print("N[{0}] = {1}".format(pos,l))
    pos += 1