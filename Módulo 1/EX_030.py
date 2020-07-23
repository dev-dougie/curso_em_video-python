print('É bissexto ou não é?')
print('-'*30)

ano = int(input('Por favor, digite um ano qualquer. Ex: 1950 --> '))

if ano % 4 == 0 or ano % 400 == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print(f'{ano} não é um ano bissexto.')