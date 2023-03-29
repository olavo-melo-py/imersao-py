'''
IMERSÃO EM PYTHON - Especialização em Dados - 2023.1

AULA 01 - Lista de exercícios 01 - Exercício 07 -- 28/03/2023
Duração de uma partida de Xadrez

'''

hora_inicio = int(input("Digite a hora do início do jogo : "))
hora_fim = int(input("Digite a hora do final do jogo : "))



if hora_inicio < hora_fim:
    duracao = hora_fim - hora_inicio
elif hora_inicio > hora_fim:
    duracao = hora_fim + (24 - hora_inicio)
else:
    duracao = 24

print("Jogo com", duracao, "de duração")