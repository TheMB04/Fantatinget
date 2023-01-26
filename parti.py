from politiker import Politiker

class Parti:
    def __init__(self, navn, mine_politikere):
        self.navn = navn
        self.mine_politikere = mine_politikere


    def parti_verdi(self):
        self.verdi = 0
        for politiker in self.mine_politikere:
            self.verdi += politiker.return_verdi()
        return self.verdi


    def hent_poeng(self):
        poeng = self.overskrifter
        return poeng


    def hent_mitt_parti(self):
        for politiker in self.mine_politikere:
            print(f"{politiker.hent_navn()} - Parti: {politiker.hent_parti()} | Verdi: {politiker.hent_verdi()} | Iq: {politiker.hent_iq()}")

