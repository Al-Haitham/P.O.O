from src.MyClasses import Commande, CommandeAvecRemise

#Instanciation
cmd1=Commande("cmd1",100,5)
cmdRem1=CommandeAvecRemise("cmdRem1",100,5,10)
print(cmd1.afficherC())
print(cmdRem1.afficherCR())
print(f"{Commande.calcul_totale(cmd1)}-{int(CommandeAvecRemise.calcul_totale(cmdRem1))}={int(Commande.calcul_totale(cmd1)-CommandeAvecRemise.calcul_totale(cmdRem1))}$ sauvé")