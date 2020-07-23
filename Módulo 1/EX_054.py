maior = 0
menor = 0
for x in range(1, 6):
    peso = float(input('Por favor, nos indque o peso da {}º pessoa: '.format(x)))
    if x == 1:
        maior = x
        menor = x
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso foi de {}kg'.format(maior))
print('O menor peso foi de {}kg'.format(menor))
