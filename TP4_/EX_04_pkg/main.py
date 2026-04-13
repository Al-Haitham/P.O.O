from src.MyClasses import Utilisateur,UtilisateurSimple,Administrateur

#Instanciation
user1=Utilisateur("Bob","bob@email.here")
userS1=UtilisateurSimple("Mike","mikkke@email.here","débutant")
admin1=Administrateur("jake","jakkke@email.here","total")
print(Utilisateur.afficher(user1))
print(userS1.afficherRole())
print(UtilisateurSimple.afficher(userS1))
print(admin1.afficherRole())
print(Administrateur.afficher(admin1))