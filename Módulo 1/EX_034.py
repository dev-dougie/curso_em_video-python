####################FASE12#####################
#Condições aninhadas

val_casa = float(input('Por favor, informe o valor do imóvel(R$): '))
val_sal = float(input('Por favor, iforme o seu salário(R$): '))
anos = int(input('Por favor, informe em quantos anos você pretender quitar o imóvel: '))
val_mens = (val_casa) / (anos * 12)

if val_mens > val_sal * 0.3:
    print('Infelizmente você não poderá usar o empréstimo.')
    print('\033[35mO valor da mensalidade durante {} anos será de R${:.2f}\033[m'.format(anos, val_mens))
else:
    print('Empréstimo concebido! Aguarde enquanto entramos em contato com o gerente...')


