from src.MyClasses import livre

#Instanciation
liv1=livre(0,"The Art of War","Sun Tzu",128,50)
liv2=livre(1,"Prince of Thorns","Mark Lawrence",336,100)

print(livre.__doc__)

liv1.affiche_Livre()
liv2.affiche_Livre()


liv1.set_LivPrx(80)
print(liv1.moy_prx_page())
livre.biblio_Nom("TechBiblio")
print(liv1.biblio)
print(liv2.biblio)