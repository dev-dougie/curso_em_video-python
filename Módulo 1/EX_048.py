print('TABUADA')
print('-='*30)
s = 0
num = int(input('Digite o número que você deseja saber a tabuada: '))
for x in range(1, 11):
    m = x * num
    print("{} x {} = \033[36m{}\033[m".format(num, x, m))
print('-='*30)
print('FIM')
