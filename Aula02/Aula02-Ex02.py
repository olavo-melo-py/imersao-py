"""
Dominó
"""


jogador1 = int(input("pontos do jogador 1: "))
jogador2 = int(input("pontos do jogador 2: "))
jogador3 = int(input("pontos do jogador 3: "))
jogador4 = int(input("pontos do jogador 4: "))


if (jogador1 > jogador2) & (jogador1 > jogador3) & (jogador1 > jogador4): 
    print("Jogador(a) 1 que venceu com", jogador1, "ponto(s)")
elif (jogador2 > jogador1) & (jogador2 > jogador3) & (jogador2 > jogador4): 
    print("Jogador(a) 2 que venceu com", jogador2, "ponto(s)")
elif (jogador3 > jogador1) & (jogador3 > jogador2) & (jogador3 > jogador4): 
    print("Jogador(a) 3 que venceu com", jogador3, "ponto(s)")
elif (jogador4 > jogador1) & (jogador4 > jogador2) & (jogador4 > jogador3): 
    print("Jogador(a) 4 que venceu com", jogador4, "ponto(s)")
else:
    print("Pode ter acontecido um empate....")