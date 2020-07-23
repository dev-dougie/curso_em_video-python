print('É par ou ímpar?')
print('='*30)

num = float(input('Digite um valor qualquer: '))
print('\033[35m{}\033[m é par'.format(num) if num % 2 == 0 else "\033[36m{}\033[m é impar".format(num))
