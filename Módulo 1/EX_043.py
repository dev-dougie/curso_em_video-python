preco = float(input('Digite o preço do produto: '))
print('CONDIÇÃO DE PAGAMENTO: ')
print('1 - À vista no dinheiro \n2 - À vista no cartão \n3 - Em até 2x no cartão \n4 - 3x ou mais')
op = int(input('Digite a opção: '))

if op == 1:
    desc_10 = preco - (preco * 0.1)
    print('O cliente recebeu 10% de desconto no produto. Agora irá pagar: R${}'.format(desc_10))
elif op ==2:
    desc_05 = preco - (preco * 0.05)
    print('O cliente recebeu 5% de desconto no produto. Agora irá pagar: R${}'.format(desc_05))
elif op == 3:
    print('O cliente não recebeu desconto no produto. Portanto pagará seu preço normal: R${}'.format(preco))
elif op == 4:
    acres_20 = preco + (preco * 0.2)
    print('O cliente pagará 20% de juros sobre o valor total da compra. Pagando assim R${}'.format(acres_20))