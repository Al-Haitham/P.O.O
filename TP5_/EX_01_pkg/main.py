from src.MyClasses import chaine,phrase

#Instanciation
ch1=chaine("bonjour")
chf=phrase("bonjour le monde!","francais")
che=phrase("hello world?","english")
print(chaine.afficher(ch1))
print(phrase.afficher(chf))
print(phrase.afficher(che))
print(phrase.type(chf))
print(phrase.type(che))
print(phrase.longueurMot(chf))
print(phrase.longueurMot(che))