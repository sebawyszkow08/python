class przedmiot():
    nazwa = ""
    srednia = 0

    def stwuzliste(self):
        self.oceny = []

    def dodajo(self,ocena):
        self.oceny.append(ocena)
        self.srednia = sum(self.oceny) / len(self.oceny)

    def w_oceny(self):
        return self.oceny 
    
    def w_srednia(self):
        return self.srednia
    
    def usun_ocene(self,usuwana_ocena):
        print( self.oceny)
        
        self.oceny.pop(usuwana_ocena)




