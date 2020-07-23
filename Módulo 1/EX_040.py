print('SAIBA A SUA CATEGORIA!')

ano_nasc = int(input('Digite o seu ano de nascimento: '))
ano = 2020
cat = ano -  ano_nasc

if cat <= 9:
    print('Categoria: MIRIM')
elif (cat > 9) and (cat <= 14):
    print('Categoria: INFANTIL')
elif (cat > 14 ) and (cat <= 19):
    print('Categoria: JUNIOR')
elif (cat >19) and (cat <=20):
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
