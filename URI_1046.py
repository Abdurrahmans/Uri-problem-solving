start, end = map(int,input().split())
if start>= end:
    end = end+24
    start = end-start
    print ('O JOGO DUROU {} HORA(S)'.format(start))
else:
    start = end-start
    print ('O JOGO DUROU {} HORA(S)'.format(start))
