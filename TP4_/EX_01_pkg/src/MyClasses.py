class personne:
    def __init__(self,nom="--",prenom="--",age=0):
        self.nom=nom
        self.prenom=prenom
        self.age=age
    
    def get_nom(self):
        return self.nom
    
    def get_prenom(self):
        return self.prenom

    def get_age(self):
        return self.age

    def set_nom(self,nom):
        self.nom=nom

    def set_prenom(self,prenom):
        self.prenom=prenom

    def set_age(self,age):
        self.age=age
    
    def afficher(self):
        print(f"nom: {self.nom}\nprenom: {self.prenom}\nage: {self.age}") 

class directeur(personne):
    def __init__(self,nom,prenom,age,salaire):
        super().__init__(nom,prenom,age)
        #personne.__init__(self, nom, prenom, age)
        self._salaire=salaire
    
    def get_salaire(self):
        return self._salaire
    
    def set_salaire(self,salaire):
        self._salaire=salaire
    
    def afficher(self):
        super().afficher()
        print(f"salaire: {self._salaire}")