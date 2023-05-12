
perguntas = []
suspeito = 0
resp = "S"
c =0 

while resp == "S":
    respostas = [
        input("Voce ligou para a vitima: ").upper(),
        input("Esteve no local do crime?: ").upper(),
        input("Mora perto da vítima?: ").upper(),
        input("Devia para a vítima?: ").upper(),
        input("Já trabalhou com a vítima?: ").upper()
    ]

    perguntas.append(respostas)
    resp ="N"

for elemento in perguntas:
    if elemento[0] == "S":
        suspeito+=1

for elemento in perguntas:
    if elemento[1] == "S":
        suspeito+=1

for elemento in perguntas:
    if elemento[2] == "S":
        suspeito+=1

for elemento in perguntas:
    if elemento[3] == "S":
        suspeito+=1

for elemento in perguntas:
    if elemento[4] == "S":
        suspeito+=1

if suspeito < 2 :
    print("INOCENTE")

if suspeito == 5 :
    print("ASSASINO")
    

if suspeito >=2 and suspeito < 3:
    print("SUSPEITO")

if suspeito >=3 and suspeito <=4:
    print("CUMPLICE")








