from politiker import Politiker
import json

class Parti:
    def __init__(self, navn, overskrifter, alle_politikere):
        self.navn = navn
        self.overskrifter = overskrifter


    def parti_verdi(self):
        verdi = politiker[]
        return verdi


    def hent_poeng(self):
        poeng = self.overskrifter
        return poeng



fil = open("politikere.json", encoding="utf-8")
politikere = json.load(fil)
fil.close()

alle_politikere = []

for i in range(0, len(politikere["representanter_oversikt"]["representanter_liste"]["representant"])):
    politiker = Politiker((politikere["representanter_oversikt"]["representanter_liste"]["representant"][i]["fornavn"] + politikere["representanter_oversikt"]["representanter_liste"]["representant"][i]["etternavn"]), politikere["representanter_oversikt"]["representanter_liste"]["representant"][i]["parti"]["navn"])
    alle_politikere.append(politiker)   

Høyre = Parti("Høyre", 0, alle_politikere)