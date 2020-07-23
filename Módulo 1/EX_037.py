from datetime import date

data_atual = date.today()
date_em_texto = data_atual.strftime('%d/%m/%y')
print(date_em_texto)
print('-'*30)
print('Serviço militar')
print('>_'*30)
ano_nasc = int(input('Digite o seu ano de nascimento: '))
ano = int(input('Digite o ano atual: '))
idade = ano - ano_nasc
idade_menor = 18 - idade
idade_maior = idade - 18
alistamento = 18

if alistamento == idade:
    print('Você tem {} idade e portanto deve se apresentar nas forças armadas este ano.'.format(idade))
elif idade < alistamento:
    print('Ainda faltam {} anos para você se apresentar.'.format(idade_menor))
elif idade > alistamento:
    print('Já se passaram {} anos! Caso não tenha se alistado, apresente-se agora.'.format(idade_maior))
