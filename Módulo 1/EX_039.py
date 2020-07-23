print('\033[35mMédia dos alunos.\033[m')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

if m < 5.0:
    print('\033[31mREPROVADO!!\033[m')
elif (m > 5.0) and (m <= 6.9):
    print('\033[33mRECUPERAÇÃO!!\033[m')
else:
    print('\033[34mAPROVADO!!\033[m')