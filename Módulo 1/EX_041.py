print('Pode ou não formar um triângulo?')
print('OBS: se o comprimento desejado é em m, obrigatoriamente todas as retas precisam ser em metros.')
print("°"*30)
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da primeira reta: '))
r3 = float(input('Digite o comprimento da primeira reta: '))
validation = r1 + r2
if validation > r3:
    print('\033[1;34;42mPode-se formar uma triângulo!\033[m')
else:
    print('\033[1;0;41mNão se pode formar um triângulo.\033[m')

if r1 == r2 == r3:
    print('Triângulo equilátero.')
elif (r1 == r2) or (r1 == r3) or (r2 == r3):
    print('Triângulo isósceles.')
elif (r1 != r2) or (r1 != r3) or (r2 != r3):
    print('Triângulo escaleno')