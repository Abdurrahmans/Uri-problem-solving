amount = int(input())

print(amount)
print('{} nota(s) de R$ 100,00'.format(int(amount/100)))
notes = amount%100
print('{} nota(s) de R$ 50,00'.format(int(notes/50)))
notes = notes % 50
print('{} nota(s) de R$ 20,00'.format(int(notes/20)))
notes = notes % 20
print('{} nota(s) de R$ 10,00'.format(int(notes/10)))
notes = notes % 10
print('{} nota(s) de R$ 5,00'.format(int(notes/5)))
notes = notes % 5
print('{} nota(s) de R$ 2,00'.format(int(notes/2)))
notes = notes % 2
print('{} nota(s) de R$ 1,00'.format(int(notes)))
