dolar = float(input('Digite a cotação atual do dólar: '))
dinheiro = float(input('Digite a quandidade de dinheiro em reais que você possui: '))
print('Com R${} você consegue adiquirir U$${}'.format(dinheiro, dinheiro/dolar))