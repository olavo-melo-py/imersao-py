'''
IMERSÃO EM PYTHON - Especialização em Dados - 2023.1

AULA 01 - Lista de exercícios 01 - Exercício 05 -- 28/03/2023
Média2
Nota com média ponderada

'''


print('Cálculo média ponderada das notas do aluno')
print('__________________________________________')


nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

#media = ((nota1*2) + (nota2*3) + (nota3*5))/10
media = (nota1*2 + nota2*3 + nota3*5)/10
print("MÉDIA = ", media)