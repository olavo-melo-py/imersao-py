"""
Jogo da palavra embaralhada

"""

import random

embpal = ""
#palavra = input("digite uma palavra : ")

lista_de_palavras = ["banana","laranja","bola","olavo","escola", "cesar", "python"]

len_lista_de_palavras = len(lista_de_palavras)

r = random.randrange(0,len_lista_de_palavras)

palavra = lista_de_palavras[r]

emblist = palavra
random.shuffle(emblist)
print(emblist)
for x in emblist:
    embpal = embpal + x

print("Palavra embaralhada: ", embpal)

x = 0
while x < 6:
    tentativa = input("tentativa = ") 
    if tentativa == emblist:
        print("Você acertou !!!!")
        break 
    elif (tentativa != emblist):        
        if x == 5: 
            print("Errou 6 vezes, você Perdeu!")
            break
        elif x < 6:
            print("Errou !!!! tente outra vez...")
            x += 1
