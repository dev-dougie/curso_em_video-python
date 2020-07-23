import time
print('Realizando cálculos entre dois valores!')
maior = 0
op = -1
while op != 5:
    print('[1] - Somar \n[2] - Multiplicar \n[3] - Maior \n[4] - Novos números \n[5] - Sair do programa')
    op = int(input("Informe sua escolha: "))
    if op == 1:
        print('-----VOCÊ ESCOLHEU A 1º OPÇÂO-----')
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        soma = n1 + n2
        print('Realizando soma...')
        time.sleep(2)
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif op == 2:
        print('-----VOCÊ ESCOLHEU A 2º OPÇÃO-----')
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        mult = n1 * n2
        print('Realizando multiplicação...')
        time.sleep(2)
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, mult))
    elif op == 3:
        print("-----VOCÊ ESCOLHEU A 3º OPÇÃO-----")
        n1 = float(input('Informe um número: '))
        n2 = float(input('Informe um número: '))
        if n1 > n2:
             print('O maior número informado foi o 1º: {}'.format(n1))
        else:
            print('O maior número informado foi o 2º: {}'.format(n2))
    elif op == 4:
        print('-----VOCÊ ESCOLHEU A 4º OPÇÃO-----')
        n = float(input('Informe o número que deseja ser incluído: '))
        print('Número {} incluso com sucesso!'.format(n))
    elif op == 5:
        print('Ok, nos vemos depois!')