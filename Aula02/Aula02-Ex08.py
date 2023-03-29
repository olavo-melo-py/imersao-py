"""
Suspeito

"""

count_sim = 0

pergunta1 = input("Telefonou para a vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da vítima ? ")
pergunta4 = input("Devia para a vítima ? ")
pergunta5 = input("Já trabalhou com a vítima ? ")

if pergunta1 == "S":
    count_sim += 1


if pergunta2 == "S":
    count_sim += 1


if pergunta3 == "S":
    count_sim += 1


if pergunta4 == "S":
    count_sim += 1


if pergunta5 == "S":
    count_sim += 1


if count_sim < 2: 
    print("Inocente")
if 2 <= count_sim < 3:
    print("Suspeita")
elif 3 <= count_sim <= 4:
    print("Cúmplice")
elif count_sim == 5: 
    print("Assassino")

