'''
IMERSÃO EM PYTHON - Especialização em Dados - 2023.1

AULA 01 - Lista de exercícios 01 - Exercício 06 -- 28/03/2023
Salário dos funcionários, com bônus

'''


print('Cálculo do salário, com bônus')
print('__________________')

nome = input("Digite o nome do funcionário :")
salario_fixo = float(input("Digite o salário fixo :"))
total_de_vendas = float(input("Digite o total de vendas :"))
salario_total = salario_fixo + 0.15*total_de_vendas


print(f'TOTAL = R$ {salario_total:.2f}')