import random
a1 = str(input('Digite o nome do aluno 1: '))
a2 = str(input('Digite o nome do aluno 2: '))
a3 = str(input('Digite o nome do aluno 3: '))
a4 = str(input('Digite o nome do aluno 4: '))

alunos = [a1, a2, a3, a4]
random.shuffle(alunos) #Embaralho em ordem aleatória
print('A ordem de apresentação será: ')
print(alunos)