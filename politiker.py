import json

class Politiker:
    def __init__(self, navn, parti):
        self.navn = navn
        self.parti = parti


    def return_iq(self):
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
        else:
            self.iq = self.iq*-1
        
        return self.iq


    def return_verdi(self):
        self.verdi = 30000
        self.verdi = self.verdi*self.iq
        return self.verdi



fil = open("politikere.json", encoding="utf-8")
politikere = json.load(fil)
fil.close()

alle_politikere = []

for i in range(0, len(politikere["representanter_oversikt"]["representanter_liste"]["representant"])):
    politiker = Politiker((politikere["representanter_oversikt"]["representanter_liste"]["representant"][i]["fornavn"] + politikere["representanter_oversikt"]["representanter_liste"]["representant"][i]["etternavn"]), politikere["representanter_oversikt"]["representanter_liste"]["representant"][i]["parti"]["navn"])
    alle_politikere.append(politiker)      