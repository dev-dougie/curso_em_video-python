print('Cálculo de passagem')
dist = float(input('Por favor, digite a distância de viagem em km: '))
valor_abaixo = dist * 0.5
valor_acima = ((dist - 200) * 0.45) + 100
if dist <= 200:
    print('Você terá que pagar um valor de R${} pois sua viagem *NÂO* atingiu o limite de distância de 200km'.format(valor_abaixo))
else:
    print('Você terá que pagar um valor de R${} pois sua viagem *ATINGIU* o limite de distância de 200km'.format(valor_acima))