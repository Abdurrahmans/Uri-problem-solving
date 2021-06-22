n = int(input())
C=R=S=total = 0
for x in range(n):
    a,b =map(str,input().split())
    a = int(a)
    if b=='C':
        C +=a
    elif b=='R':
        R +=a
    else:
        S +=a
    total = C+R+S
    x = (C*100.00)/total
    y = (R * 100.00) / total
    z = (S * 100.00) / total

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(C))
print('Total de ratos: {}'.format(R))
print('Total de sapos: {}'.format(S))
print('Percentual de coelhos: {:.2f} %'.format(x))
print('Percentual de ratos: {:.2f} %'.format(y))
print('Percentual de sapos: {:.2f} %'.format(z))