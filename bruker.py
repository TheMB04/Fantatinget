class Bruker:

    def __init__(self, brukernavn, passord, epost):
        self._brukere = []
        self._brukernavn = brukernavn
        self._passord = passord
        self._epost = epost
        self._saldo = 100000

    def oek_saldo(self, antall):
        self._saldo += antall

    def hent_bruker(self):
        return self._brukernavn

    def logg_inn(self):
        pass

    def ny_bruker(self, brukernavn, passord, epost):
        pass
        #bruker = 
        #self._brukere.append(bruker)










