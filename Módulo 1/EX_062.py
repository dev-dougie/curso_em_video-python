print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)

termos = int(input('Digite a quantidade de termos que você quer mostrar: '))
t1 = 0
t2 = 1
print('↔'*30)
print('{}, {}'.format(t1, t2))
print("↔"*30)
cont = 3
while cont <= termos:
    t3 = t1 + t2
    print("→ {}".format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont = cont + 1
print("FIM")
