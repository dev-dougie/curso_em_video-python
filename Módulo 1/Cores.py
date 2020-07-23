#ANSI começa com \033[STYLE TEXT BACK m para cor
#STYLE: 0, 1, 4, 7  | TEXT: 30:37 | 40:47

num = float(input('\033[1mPor favor, digite um número: '))

if num > 0:
    print('Número \033[1;32mPOSITIVO!\033[m')
else:
    print('Número \033[1;31mNEGATIVO!\033[m')