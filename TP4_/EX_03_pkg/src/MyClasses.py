class Commande:
    def __init__(self,produit,prix_unitaire,quantite):
        self.produit=produit
        self.prix_unitaire=prix_unitaire
        self.quantite=quantite
    
    def calcul_totale(self):
        print(f"le prix totale est:{self.prix_unitaire*self.quantite}")
        return self.prix_unitaire*self.quantite

    def afficherC(self):
        print(f'produit:{self.produit} - prix unitaire:{self.prix_unitaire} - quantite:{self.quantite} - prix totale:{self.calcul_totale()}',end=" ")
    

class CommandeAvecRemise(Commande):
    def __init__(self,produit,prix_unitaire,quantite,remise):
        super().__init__(produit,prix_unitaire,quantite)
        self.remise=remise

    def calcul_totale(self):
        print(f"le prix totale avec remise est:{super().calcul_totale()*(1-self.remise/100)}")
        return super().calcul_totale()*(1-self.remise/100)
    
    def afficherCR(self):
        super().afficherC()
        print(f"- avec un remise de {self.remise}%")