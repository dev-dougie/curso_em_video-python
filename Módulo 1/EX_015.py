from math import pow, sqrt

co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
hi = pow(co, 2) + pow(ca, 2)
resp_final = sqrt(hi)

print('Com o CA valendo {}cm e CO valendo {}cm, o comprimento da hipotenusa é {:.1f}cm'.format(co, ca, resp_final))