print('PROGRAMINHA BÁSICO PARA O DEMUTRAN')
print('-*' * 30)
velocidade = float(input('Digite a velocidade atingida pelo carro: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Atingiu: {}km/h, atingindo assim a velocidade máxima de 80km/h. \nPortanto, o valor da multa será: R${:.2f}'.format(velocidade, multa))
else:
    print('Limite aceito.')