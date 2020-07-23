print('QUAL É O MAIOR VALOR?')

num1 = float(input('Por favor, digite o primeiro valor: '))
num2 = float(input('Por favor, digite o segundo valor: '))

if num1 > num2:
    print('O 1º valor é o maior: {}'.format(num1))
elif num2 > num1:
    print('O  2º valor é o maior: {}'.format(num2))
else:
    print('Não existe valor igual, os dois são iguais!')