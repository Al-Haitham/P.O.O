class CompteBancaire:

    def __init__(self,numeroCompte,nomPropr,solde):
        self.numCmpt=numeroCompte
        self.nomPropr=nomPropr
        self.soldeCmpt=solde

    def versement(self,montantVers):
        if montantVers>=0:
            try:
                self.soldeCmpt+=montantVers
            except Exception as e:
                print("erreur: ",e)

    def retrait(self,montantRetr):
        if montantRetr>=0:
            try:
                self.soldeCmpt-=montantRetr
            except Exception as e:
                print("erreur: ",e)

    def agios(self):    
        self.soldeCmpt*=(1-0.05)

    def afficher(self):
        print(f"numero du compte: {self.numCmpt}\nnom de proprietaire: {self.nomPropr}\nsolde: {self.soldeCmpt} DHS")
    
