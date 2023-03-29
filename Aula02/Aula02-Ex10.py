"""
Caixa Eletrônico

"""


saque = int(input("Digite o valor do saque : R$ "))

if saque < 10: 
    print("O valor do saque é inferior ao mínimo de R$ 10,00.")

if saque > 600:
    print("O valor do saque é superior ao máximo de R$ 600,00.")



notas_100 = saque // 100
notas_50 = (saque % 100) // 50
notas_10 = ((saque % 100) % 50) // 10
notas_5 = (((saque % 100) % 50) % 10) // 5
notas_1 = (((saque % 100) % 50) % 10) % 5


print("notas de R$ 100.00 = ", notas_100)
print("notas de R$ 50.00 = ", notas_50)
print("notas de R$ 10.00 = ", notas_10)
print("notas de R$ 5.00 = ", notas_5)
print("notas de R$ 1.00 = ", notas_1)