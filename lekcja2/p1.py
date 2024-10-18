from przedmiot import przedmiot


polski = przedmiot()
polski.stwuzliste()
polski.nazwa = "polski"

polski.dodajo(5)
polski.dodajo(1)
polski.dodajo(3)
polski.dodajo(1)

print(polski.w_oceny())
print(polski.w_srednia())

polski.usun_ocene(1)
polski.usun_ocene(2)

print(polski.w_oceny())

p_srednia = polski.w_srednia()

matma = przedmiot()
matma.stwuzliste()
matma.nazwa = "matma"

matma.dodajo(5)
matma.dodajo(5)
matma.dodajo(3)
matma.dodajo(2)

m_srednia = matma.w_srednia()

angielski = przedmiot()
angielski.stwuzliste()
angielski.nazwa = "angielski"

angielski.dodajo(2)
angielski.dodajo(1)
angielski.dodajo(1)
angielski.dodajo(1)

a_srednia = angielski.w_srednia()


alls = [p_srednia,m_srednia,a_srednia]

print(max(alls))







