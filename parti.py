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


    def hent_mitt_parti(self):
        pass  

