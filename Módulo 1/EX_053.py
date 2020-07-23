import datetime
atual = datetime.date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input('Digite o ano de nasicmento da {}º pessoa: '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1

print('{} pessoas maiores de idade'.format(totmaior))
print('{} pessoas menores de idade'.format(totmenor))