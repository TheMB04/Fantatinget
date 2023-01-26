from random import randint

class Politiker:
    def __init__(self, navn, parti):
        self.navn = navn
        self.parti = parti


    def hent_iq(self):
        self.iq = 100
        if self.parti == "Høyre":
            self.iq = self.iq*1.5
        elif self.parti == "Fremskrittspartiet":
            self.iq = self.iq*3
        elif self.parti == "Arbeiderpartiet":
            self.iq = self.iq
        elif self.parti == "Senterpartiet":
            self.iq = self.iq*0.9
        elif self.parti == "Pasientfokus":
            self.iq = self.iq*0.2
        elif self.parti == "Kristelig Folkeparti":
            self.iq = self.iq*0.8
        elif self.parti == "Rødt":
            self.iq = self.iq*0.3
        elif self.parti == "Miljøpartiet De Grønne":
            self.iq = self.iq*0.1
        elif self.parti == "Venstre":
            self.iq = self.iq*0.7
        elif self.parti == "Sosialistisk Venstreparti":
            self.iq = self.iq*0.01
       
        return self.iq


    def hent_verdi(self):
        self.verdi = 10000*randint(1, 5)
        self.verdi = self.verdi*self.hent_iq()
        return self.verdi

    
    def hent_navn(self):
        return self.navn

    
    def hent_parti(self):
        return self.parti
   