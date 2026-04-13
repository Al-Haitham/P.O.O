class personne:
    def __init__(self,nom="--",prenom="--",age=0):
        self._nom=nom
        self._prenom=prenom
        self._age=age
    
    def get_nom(self):
        return self._nom
    
    def get_prenom(self):
        return self._prenom

    def get_age(self):
        return self._age

    def set_nom(self,nom):
        self._nom=nom

    def set_prenom(self,prenom):
        self._prenom=prenom

    def set_age(self,age):
        self._age=age
    
    def afficher(self):
        print(f"nom: {self._nom}\nprenom: {self._prenom}\nage: {self._age}") 

class directeur(personne):
    def __init__(self,nom,prenom,age,salaire):
        super().__init__(nom,prenom,age)
        self._salaire=salaire
    
    def get_salaire(self):
        return self._salaire
    
    def set_salaire(self,salaire):
        self._salaire=salaire
    
    def afficher(self):
        super().afficher()
        print(f"salaire: {self._salaire}")