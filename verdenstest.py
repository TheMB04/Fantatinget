from stortinget import Verden
from politiker import Politiker
from parti import Parti
from bruker import Bruker

min_verden = Verden()

for politiker in politikerListe:
    ny_politiker = Politiker(navn, parti) 
    min_verden.append(ny_politiker)


mitt_lag = Parti("Nasjonal Blanding")
jonas = min_verden.finn_politikere("Jonas Gahr Støre")
mitt_lag.kjop(jonas)
