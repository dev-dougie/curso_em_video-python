from random import randint
computador = randint(0, 10)
print('\033[35mADVINHE O NÚMERO\033[m')
resp = int(input('Pensei em um número entre 0 e 10, você consegue adivinhar? '))
tentativas = 0
while resp != computador:
    resp = int(input('Você errou, tente novamente: '))
    tentativas += 1
print('Ufa, finalmente você descobriu que o número em que pensei foi {}. Para advinhá-lo você tentou {} vezes'.format(resp, tentativas+1))