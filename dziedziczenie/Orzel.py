import random
from Ptak import Ptak

class Orzel(Ptak):
    
    
    def __init__(self,wiek,imie):

        super().__init__(wiek,imie)
        self.doswiadczenie = 0
        self.potencjalneofiary = ["szczur","kroliczek","kosmiczna mysz","galaktyczny choimk"]
        
    def poluj(self):
        print(f"{self.imie} poluje")
        if random.randint(0,2) == 1:
            
            self.doswiadczenie += 1
            print(f"{self.imie} ma {self.doswiadczenie} doświadczenia, jego ofiarą był {random.choice(self.potencjalneofiary)}")


        else:
            print("nieupolował")



    
