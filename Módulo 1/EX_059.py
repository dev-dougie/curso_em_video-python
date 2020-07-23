print('SABENDO O FATORIAL!')
num = int(input('Digite o número o qual você deseja saber o fatorial: '))
resultado = count = 1

while count <= num:
    resultado *= count
    count += 1
print('O fatorial de {} é {}'.format(num, resultado))
