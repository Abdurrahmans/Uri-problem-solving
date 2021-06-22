s = 0
a = 1
for x in range(1,40,2):
    m = x / a
    s = s + m
    a = a * 2

print('{:.2f}'.format(s))

