"""
Aula 02
Exemplo - bilheteria do teatro

"""

idade = int(input("digite sua idade : "))

if idade < 4: 
    print("Entrada Gratuita")
elif  4 <= idade <18:
    print("A entrada custa 20 Reais")
elif 18 <= idade < 60:
    print("A entrada custa 30 Reais")
else:
    print("Entrada Gratuita")