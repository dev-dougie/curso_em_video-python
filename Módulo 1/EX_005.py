# \\ - divisão inteira          # 81 ** (1/2) = 9
# ** - exponeciação
# % - módulo ou resto da divisão

# 1 - ()
# 2 - ** | pow(x, y)
# 3 - *, /, //, %
# 4 - +, -
# {:20}, {:>20}, {:<20}, {:^20}, {:=^20}

numero = int(input('Por favor, digite um número inteiro: '))
print('O antecessor de {} é {} \nO sucessor de {} é {}.'.format(numero, numero - 1, numero, numero + 1))
