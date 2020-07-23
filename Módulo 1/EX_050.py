a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
an = a1 + (10 - 1) * r
for c in range(a1, an + r, r):
    print('{}'.format(c), end=' -> ')
print('FINISH')