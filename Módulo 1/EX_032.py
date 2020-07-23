print('Aumento salarial de acordo com o valor do salário do funcionário.')
print('=*'*30)

sal = float(input('Por favor, digite o valor do salário do funcionário: '))

if sal > 1250:
    ajuste_cima = sal * 0.1
    print("Com um aumento de 10%, o salário de R${} passou a ser de R${}".format(sal, sal + ajuste_cima))
elif sal <= 1250:
    ajuste_abaixo = sal * 0.15
    print('Com um aumento de 15%, o salário de R${} passou a ser de R${}'.format(sal, sal + ajuste_abaixo))