num = int(input('Digite um número inteiro: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        print("\033[34m", end=' ')
        total = total + 1
    else:
        print('\033[33m', end=' ')
    print(c, end=' ')

print(f'\nO número {num} foi dividido {total} vezes(por 1 e por ele mesmo)')

if total == 2:
    print("O número {} é um número primo".format(num))
else:
    print('O número {} não é um número primo'.format(num))