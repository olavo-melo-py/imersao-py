a = int(input("Digite o comprimento do lado A "))
b = int(input("Digite o comprimento do lado B "))
c = int(input("Digite o comprimento do lado C "))

if ((a+b) > c) and ((a+c) > b) and ((b+c) > a):
    print("É um triângulo!")
    if a == b == c: 
        print("É um triângulo Equilátero!")
    elif a == b or a == c or b == c: 
        print("É um triângulo Isósceles!")
    elif a != b != c: 
        print("É um triângulo Escaleno!")
else:
    print("Não é um triângulo!")