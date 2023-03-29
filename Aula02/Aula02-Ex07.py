


seq = input("digite uma sequência de caracteres :")

seq_sem_espacos = seq.replace(" ","")
print(seq_sem_espacos)

seq_len = len(seq_sem_espacos)
inv_seq = seq_sem_espacos[::-1]
print(inv_seq)

if seq_sem_espacos == inv_seq:
    print("A sequência de caracteres é um palíndromo!")
else:
    print("A sequência de caracteres NÃO É um palíndromo!")
