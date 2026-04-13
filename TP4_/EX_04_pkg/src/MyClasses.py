class Utilisateur:
    def __init__(self,nom,email):
        self.nom=nom
        self.email=email
    
    def afficher(self):
        return f'nom: {self.nom} - email: {self.email}'
    
class UtilisateurSimple(Utilisateur):
    def __init__(self,nom,email,niveau):
        super().__init__(nom,email)
        self.niveau=niveau

    def afficher(self):
        return f"{super().afficher()} - niveau: {self.niveau}"
    def afficherRole(self):
        return "Utilisateur Simple"

class Administrateur(Utilisateur):
    def __init__(self,nom,email,droit_access):
        super().__init__(nom,email)
        self.droitAccess=droit_access
    
    def afficher(self):
        return f"{super().afficher()} - droit d'access: {self.droitAccess}"
    def afficherRole(self):
        return "Administrateur"
