import random
gracz = 0
komp = 0
stronymon = ["orzel","reszka"]
while True:
    rzut = input("orzel czy reszka")
    rzukomp = stronymon[random.randint(0,1)]

    moneta = stronymon[random.randint(0,1)]

    if rzut == moneta :
        gracz += 1

    if rzukomp == moneta:
        komp += 1


    print(moneta)

    print("gracz ", gracz)
    print("komp ", komp)