from Zwierze import Zwierze


class Kot(Zwierze):

    def __init__(self,wiek,imie,rasa):

        super().__init__(wiek,imie)
        self.rasa = rasa


    def wypiszrase(self):
        print(f"{self.rasa} to rasa naszego futrzaka")



