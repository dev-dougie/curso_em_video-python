print('Cálculo de IMC')

peso = float(input('Informe seu peso: '))
altura = float(input("Informe sua altura: "))
IMC = peso / (altura * altura)

if IMC < 18.5:
    print('Abaixo do peso!')
elif (IMC > 18.5) and (IMC < 25):
    print('Peso Ideal!')
elif (IMC >= 25) and (IMC <= 30):
    print('Sobrepeso!')
elif (IMC > 30) and (IMC <= 40):
    print('Obesidade!')
else:
    print('Obesidade mórbida!')