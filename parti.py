from politiker import Politiker
import json

class Parti:
    def __init__(self, navn, mine_politikere):
        self.navn = navn
        self.mine_politikere = mine_politikere


    def parti_verdi(self):
        self.verdi = 0
        for min_politiker in self.mine_politikere:
            self.verdi += min_politiker.return_verdi()
        return self.verdi


    def hent_poeng(self):
        poeng = self.overskrifter
        return poeng



overskrifter = 0

fil = open("politikere.json", encoding="utf-8")
politikere = json.load(fil)
fil.close()

alle_politikere = []
mine_politikere = []

for i in range(0, len(politikere["representanter_oversikt"]["representanter_liste"]["representant"])):
    politiker = Politiker((politikere["representanter_oversikt"]["representanter_liste"]["representant"][i]["fornavn"] + politikere["representanter_oversikt"]["representanter_liste"]["representant"][i]["etternavn"]), politikere["representanter_oversikt"]["representanter_liste"]["representant"][i]["parti"]["navn"])
    alle_politikere.append(politiker)   

mitt_parti = Parti(input("Hva skal partiet ditt hete?"), mine_politikere)