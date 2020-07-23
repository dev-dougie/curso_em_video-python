#utiliza-se while quando não há limite definido
"""while <valor> != variavel:
    do something""" #flag

sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, nos indique um valor válido para sexo: '))
print('Dados validados com sucesso!')