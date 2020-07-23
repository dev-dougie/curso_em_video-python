#laços de repetição. (iteração)
#USO DO FOR: for c in range(0, 5) - inicia-se de 1 até 5
import time

print('Contagem regressiva para os fogos de artíficio!')
for c in range(10, 0, -1):
    time.sleep(1)
    print(c)
print('\033[35m🎆🎆🎆🎆🎆🎆🎆\033[m')
