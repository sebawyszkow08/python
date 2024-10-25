from Zwierze import Zwierze

class pies(Zwierze):


    def __init__(self,wiek,imie,rasa):

        super().__init__(wiek,imie)
        self.rasa = rasa




    def wypiszrase(self):
        print(f"{self.rasa} to rasa naszego psa")



     
    pass




