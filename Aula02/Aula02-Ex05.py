import datetime


dia = int(input("Digite o dia : "))
mes = int(input("digite o mês : "))
ano = int(input("digite o ano : "))

x = datetime.datetime(ano, mes, dia)

dia_eng = x.strftime("%A")

if dia_eng == "Sunday": 
    dia_pt = "Domingo"
elif dia_eng == "Monday":
    dia_pt = "Segunda-feira"
elif dia_eng == "Tuesday":
    dia_pt = "Terça-feira"
elif dia_eng == "Wednesday":
    dia_pt = "Quarta-feira"
elif dia_eng == "Thursday":
    dia_pt = "Quinta-feira"
elif dia_eng == "Friday":
    dia_pt = "Sexta-feira"
elif dia_eng == "Saturday":
    dia_pt = "Sábado"
else:
    print("erro")

print(dia_pt)
