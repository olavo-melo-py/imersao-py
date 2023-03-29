'''
IMERSÃO EM PYTHON - Especialização em Dados - 2023.1

AULA 01 - Lista de exercícios 01 - Exercício 09 -- 28/03/2023
Nota por conceito

'''

print('Nota - Média de 4 notas')
print('_______________________')

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print("---")

print("MÉDIA = ", media)

print("---")

if (media >= 9 and media <= 10):
    conceito = 'A'
elif (media >= 7.5 and media < 9):
    conceito = 'B'
elif (media >= 6.0 and media < 7.5):
    conceito = 'C'
elif (media >= 4.0 and media < 6.0):
    conceito = 'D'
elif (media >= 0.0 and media < 4.0):
    conceito = 'E'

print ("O estudante ficou com o conceito", conceito)


