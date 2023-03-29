"""
Nome Completo -> primeiro e último nome

"""

nome_completo = input("Digite seu nome completo : ")


nome_split = nome_completo.split(" ")
print("Primeiro nome : ", nome_split[0])

nome_split_last = len(nome_split) - 1
print("Último nome: ", nome_split[nome_split_last])