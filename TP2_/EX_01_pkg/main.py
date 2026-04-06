from src.MyClasses import CompteSecurise

#Instanciation
compte1=CompteSecurise(1,"haitam","123456")

imdp=input("mot de passe: ")
compte1.verifier_mot_de_passe(imdp)

compte1.changer_mot_de_passe("123457","987654")
print(CompteSecurise.affiche_compte(compte1))