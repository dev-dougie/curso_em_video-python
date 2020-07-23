somaidade = 0
mediaidade = 0
maisvelho = 0
nomevelho = ''
menorque20 = 0
nomenova = ''
for p in range(1, 5):
    print('-----{}ºPESSOA-----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaidade += idade
    if p == 1 and sexo == "M":
        maisvelho = idade
        nomevelho = nome
    if sexo == "M" and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    if sexo == "F" and idade < 20:
        idade = menorque20
        menorque20 += 1
        nomenova = nome
mediaidade = somaidade / 4
print('A média da idade dos grupos é de {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maisvelho, nomevelho))
print('Existem {} mulheres com menos de 20 anos'.format(menorque20))
