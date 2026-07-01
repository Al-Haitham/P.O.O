import re

adresse = "Rue 41 de la République Marrakech Maroc"

listAd=re.split(r"\s",adresse)
print(listAd)

listAd2=re.split(r"\s",adresse,2)
print(listAd2)