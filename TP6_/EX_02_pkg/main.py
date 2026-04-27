from src.MyClasses import *

#Instanciation
Chiron=voiture("Bugatti",380)
YZF_R7=moto("Yamaha",224)

Chiron.afficher_infos()
Chiron.demarrer()
print(Chiron.calculer_vitesse())

YZF_R7.afficher_infos()
YZF_R7.demarrer()
print(YZF_R7.calculer_vitesse())
