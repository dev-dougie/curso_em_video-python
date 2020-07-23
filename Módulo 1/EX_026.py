from random import randint

sorteio = randint(0, 5)
user = int(input('Pensei em um número entre 0 e 5, você consegue me dizer qual número é esse? ->'))

print('Haha, você errou! Tente depois quando tiver mais sorte.' if user != sorteio else "UAU, você é bom mesmo!")