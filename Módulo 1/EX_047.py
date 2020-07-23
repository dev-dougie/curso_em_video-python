s = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
print('A soma total de todos os números ímpares, múltiplos de 3 no intervalo entre 1 e 500 é: {}'.format(s))
