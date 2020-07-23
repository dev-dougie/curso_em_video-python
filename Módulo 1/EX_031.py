print('Qual é o maior número e qual o menor?')
print('^='*30)

maior = 0

num1 = float(input('Por favor, digite o 1º número: '))
num2 = float(input('Por favor, digite o 2º número: '))
num3 = float(input('POr favor, digite o 3º número: '))

if num1 > num2 and num1 > num3:
    maior = num1
    print("O 1º número é maior. Valor {}".format(maior))
elif maior > num2 and maior > num3:
    maior = num2
    print("O 2º número é o maior. Valor {}".format(maior))
else:
    maior = num3
    print("O 3º número é o maior. Valor {}".format(maior))