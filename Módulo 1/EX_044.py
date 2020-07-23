from random import randint
from pygame import mixer
mixer.init()
mixer.music.load('ex_19.mp3')
mixer.music.play()
print("1 - Pedra \n2 - Papel \n3 - Tesoura")
op = int(input("Escolha a sua opção: "))
pc = randint(1, 3)
print("COMPUTADOR: {}".format(pc))

if op == pc:
    print('=-' * 30)
    print("Empate")
elif ((op == 1) and (pc == 2)) or (op == 2) and (pc == 3) or (op == 3) and (pc == 1):
    print('=-' * 30)
    print("\033[31mVOCÊ PERDEU!\033[m")
elif ((op == 2) and (pc == 1)) or ((pc == 3) and (op == 1) or ((pc == 1) and (op == 3) or (op == 3) and (pc == 2))):
    print('=-' * 30)
    print('\033[32m VOCÊ VENCEU!\033[m')
input('ENTER PARA FINALIZAR')