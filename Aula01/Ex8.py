'''
IMERSÃO EM PYTHON - Especialização em Dados - 2023.1

AULA 01 - Lista de exercícios 01 - Exercício 08 -- 28/03/2023
CONVERSÃO DE TEMPO
de Inteiro para HH:MM:SS

'''

print('Conversão de tempo')
print('__________________')

tempo_em_segundos = int(input("Digite o tempo do evento em segundos : "))

HH = (tempo_em_segundos // (60*60))                                  
MM = (tempo_em_segundos % (60*60)) // 60            
SS = (tempo_em_segundos % (60*60)) % 60

print(HH , ":" , MM , ":" , SS)
