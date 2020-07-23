#Caracter precisam estar entre aspas '' - String
#Fatiamento = frase[9] | frase[9:13] "sempre um a menos no final"(range)
#frase[9:21:2] | frase[:5] | frase[0:] | frase[9::3]
#ANALISE =  len(frase) | frase.count('o') | frase.count('o', 0, 13) | frase.find('deo') - diz a posição | 'Curso' in frase - True or False
#TRANSFORMAÇÃO = frase.replace('Python', 'Android') | frase.upper() | frase.lower() | frase.capitalize() - Só o 1º fica maiúscula | frase.title()
#todo começo de frase fica maísuculo | frase.strip() | frase.rstrip() | frase.lstrip()
#DIVISÂO =  frase.split() - gera uma lista com todas as palavras
#JUNÇÃO = '-'.join(frase)

nome = str(input('Digite o seu nome: ')).strip()
print('Seu nome com todas as letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas é {}'.format(nome.lower()))
splitado = nome.split()
print('Seu primeiro nome possui {} letras'.format(len(splitado[0])))
print('Seu nome completo possui {} letras'.format(len(nome) - nome.count(' ')))
