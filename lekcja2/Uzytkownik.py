class Uzytkownik():
    imie = ""
    nazwisko = ""
    wiek = 0

    def wyswietl(self):
        print(self.imie,self.nazwisko)
        if self.wiek >= 18:
            print("pelnoletni")

        else:
            print("niepelnoletni")

        print()

    def zmienwiek(self,nowywiek): 
        self.wiek = nowywiek













