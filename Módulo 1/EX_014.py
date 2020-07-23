#ceil faz um arredondamento para cima | floor para baixo
#trunc vai truncar o número
#pow = potência
#sqrt | #factorial | random da classe random gera um número entre 0 e 1

from math import floor
num = float(input('Digite um número real qualquer: '))
inteiro = floor(num)
print('A parte real inteira de {} é {}'.format(num, inteiro))