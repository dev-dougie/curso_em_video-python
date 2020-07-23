from math import radians, sin, cos, tan

ang = float(input('Digite um ângulo qualquer: '))
sen = sin(radians(ang)) #aninhando uma chamada em outra!!!!
cos = cos(radians(ang))
tng = tan(radians(ang))


print(f'O Seno de {ang} é {sen:.2f} \nO Cosseno de {ang} é {cos:.2f} \nA tangente de {ang} é {tng:.2f}')