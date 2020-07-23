print("SOMANDO APENAS NÚMEROS PARES")
print('-'*30)
s = 0
for i in range(1, 7):
    num = int(input('Por favor digite um número inteiro: '))
    if num % 2 == 0:
        s += num
print("A soma dos número pares digitados foi: {}".format(s))