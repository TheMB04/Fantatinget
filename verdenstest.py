from stortinget import Verden
from politiker import Politiker
from parti import Parti
from bruker import Bruker
import json

min_verden = Verden()
mine_politikere = []
alle_politikere = []


fil = open("politikere.json", encoding="utf-8")
politikere = json.load(fil)
fil.close()


for i in range(0, len(politikere["representanter_oversikt"]["representanter_liste"]["representant"])):
    politiker = Politiker((politikere["representanter_oversikt"]["representanter_liste"]["representant"][i]["fornavn"] + politikere["representanter_oversikt"]["representanter_liste"]["representant"][i]["etternavn"]), politikere["representanter_oversikt"]["representanter_liste"]["representant"][i]["parti"]["navn"])
    alle_politikere.append(politiker) 

mine_politikere.append(alle_politikere[0])

mitt_parti = Parti(input("Hva skal partiet ditt hete?"), mine_politikere)

mitt_parti.hent_mitt_parti()


#mitt_lag = Parti("Nasjonal Blanding")
#jonas = min_verden.finn_politikere("Jonas Gahr Støre")
#mitt_lag.kjop(jonas)



