from src.MyClasses import CompteBancaire


#Instanciation
compte1=CompteBancaire(10000000001,"Haitam",700000)

print(compte1.afficher())
compte1.versement(50000)
compte1.retrait(22000)
compte1.agios()
print(compte1.afficher())