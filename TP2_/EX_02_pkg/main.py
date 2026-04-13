from src.MyClasses import SalleCinema

#Instanciation
sall1=SalleCinema("salle1",80,20)
print(sall1.afficher())
sall1.reserver(30)
print(SalleCinema.taux_remp(sall1))