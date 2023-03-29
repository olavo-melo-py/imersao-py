nome = input("Digite seu nome : ")
idade = int(input("Digite sua idade :"))
contagiosa = input("Possui doença contagiosa, digite S ou N :")

if idade >= 65: 
    print("Atendimento com prioridade")
    if contagiosa == "S" or contagiosa == "s":
        print("Sala AMARELA")
    else:
        print("Sala BRANCA")
else: 
    print("Atendimento sem prioridade")
    if contagiosa == "S" or contagiosa == "s":
        print("Sala AMARELA")
    else:
        print("Sala BRANCA")