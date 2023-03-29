"""
Valida CPF

"""


cpf = input("Digite seu CPF no formato xxx.xxx.xxx-xx ")

n1 = int(cpf[:1])
print (n1)

n2 = int(cpf[1:2])
print (n2)

n3 = int(cpf[2:3])
print (n3)

n4 = int(cpf[4:5])
print (n4)

n5 = int(cpf[5:6])
print (n5)

n6 = int(cpf[6:7])
print (n6)

n7 = int(cpf[8:9])
print (n7)

n8 = int(cpf[9:10])
print (n8)

n9 = int(cpf[10:11])
print (n9)

d1 = int(cpf[12:13])
print(d1)

d2 = int(cpf[13:14])
print(d2)


# primeiro digito

sum1 = n1*10 + n2*9 + n3*8 + n4*7 + n5*6 + n6*5 + n7*4 + n8*3 + n9*2
print(sum1)
resto11 = 11 - (sum1 % 11)
if resto11 > 9: 
    d1_calculado = 0
else: 
    d1_calculado = resto11

if d1 == d1_calculado:
    print("Primeiro dígito correto!")
else: 
    print("Primeiro dígito inválido!")


# segundo dígito 

sum2 = n1*11 + n2*10 + n3*9 + n4*8 + n5*7 + n6*6 + n7*5 + n8*4 + n9*3 + d1*2
print(sum2)
resto11_2 = 11 - (sum2 % 11)
if resto11_2 > 9: 
    d2_calculado = 0
else: 
    d2_calculado = resto11_2

if d2 == d2_calculado:
    print("Segundo dígito correto!")
else: 
    print("Segundo dígito inválido!")

