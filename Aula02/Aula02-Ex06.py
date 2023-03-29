nome = input("Digite o nome :")
idade = int(input("Digite a idade :"))
salario = float(input("Digite o salario :"))

len_nome = len(nome)
if len_nome > 3:
    nome_ok = True
else:
    nome_ok = False


if 0 < idade < 150: 
    idade_ok = True
else:
    idade_ok = False


if salario > 0: 
    salario_ok = True
else: 
    salario_ok = False


if nome_ok and idade_ok and salario_ok: 
    print("Dados Corretos:")
else:
    print("Dados incorretos:")


if nome_ok:
    print("Nome: ", nome)
else: 
    print("Nome: incorreto")

if idade_ok:
    print("Idade: ", idade)
else:
    print("Idade: incorreta")
    
if salario_ok:
    print("Salário: ", salario)
else:
    print("Salário: incorreto")
