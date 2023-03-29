'''
IMERSÃO EM PYTHON - Especialização em Dados - 2023.1

AULA 01 - Lista de exercícios 01 - Exercício 04 -- 28/03/2023
Salário dos funcionários

'''


print('Cálculo do salário')
print('__________________')

nome = input("Digite o nome do funcionário :")
horas_trabalhadas = int(input("Digite o número de horas trabalhadas :"))
valor_hora = float(input("Digite o valor da hora de trabalho :"))

salario = horas_trabalhadas * valor_hora

print("Nome: ", nome)
print("SALÁRIO = R$", salario)
