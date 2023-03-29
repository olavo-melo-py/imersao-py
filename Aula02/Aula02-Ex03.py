"""
DC x Marvel
"""

votosDC = 0
votosMarvel = 0

voto1 = input("DC ou Marvel ? ")
voto2 = input("DC ou Marvel ? ")
voto3 = input("DC ou Marvel ? ")
voto4 = input("DC ou Marvel ? ")
voto5 = input("DC ou Marvel ? ")

if voto1 == "DC": 
    votosDC += 1
elif voto1 =="Marvel":
    votosMarvel += 1
else:
    print("Voto1 inválido!")


if voto2 == "DC": 
    votosDC += 1
elif voto2 =="Marvel":
    votosMarvel += 1
else:
    print("Voto2 inválido!")

if voto3 == "DC": 
    votosDC += 1
elif voto3 =="Marvel":
    votosMarvel += 1
else:
    print("Voto3 inválido!")

if voto4 == "DC": 
    votosDC += 1
elif voto4 =="Marvel":
    votosMarvel += 1
else:
    print("Voto4 inválido!")


if voto5 == "DC": 
    votosDC += 1
elif voto5 =="Marvel":
    votosMarvel += 1
else:
    print("Voto5 inválido!")


pct_DC = votosDC / 5 * 100
pct_Marvel = votosMarvel / 5 * 100


print("-----\n")
print(pct_DC, "% preferem DC")
print(pct_Marvel, "% preferem Marvel")
print("-----\n")
