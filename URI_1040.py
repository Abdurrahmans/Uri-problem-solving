N1,N2,N3,N4 = map(float,input().split())
average = (N1*2+N2*3+N3*4+N4*1)/(2+3+4+1)
print('Media: {:.1f}'.format(average))
if average >= 7.0:
    print ('Aluno aprovado.')
elif average < 5.0:
    print('Aluno reprovado.')
elif average >= 5.0 and average <= 6.9:
    print('Aluno em exame.')
    N = float(input())
    print('Nota do exame: {:.1F}'.format(N))
    N = (N+average)/2

    if N >= 5.0:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(N))
    elif N <= 4.9:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(N))

