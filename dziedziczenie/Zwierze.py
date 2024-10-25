class Zwierze:


    def __init__(self,wiek,imie):
        self.wiek = wiek
        self.imie = imie


    def wydajdzwiek(self):
        print(f"{self.imie} wydaje dzwięk")

    def jedzonko(self):
        print(f"{self.imie} je koperek")

    def wypiszwiek(self):
        print(f"{self.imie} ma {self.wiek} lat")

    pass