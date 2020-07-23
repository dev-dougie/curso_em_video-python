p = str(input('Digite a palavra ou frase: ')).strip().upper()
frase = p.split()
junto = ''.join(frase)
inverso = ''
for c in range(len(junto) - 1, -1, -1): #lendo a quantidade de letras em 'junto' - 1
    inverso = inverso + junto[c]
if inverso == junto:
    print('É um políndromo')
else:
    print('Não é um políndromo')
