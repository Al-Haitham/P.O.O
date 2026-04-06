class CompteSecurise:

    def __init__(self,id,nom,mdp):
        self.id=id
        self.nom=nom
        self.__mot_de_passe=mdp
        self.__tentative=0

    def get_mdp(self):
        return self.__mot_de_passe
    def set_mdp(self,n_mdp):
        self.__mot_de_passe=n_mdp

    def get_tent(self):
        return self.__tentative
    def set_tent(self,n_tent):
        self.__tentative=n_tent

    def verifier_mot_de_passe(self,mdp):
        while self.__tentative<3:
            
            if mdp==self.get_mdp():
                print("Accès autorisé!")
                break
            elif mdp!=self.get_mdp():
                
                self.set_tent(self.get_tent() + 1)
                print("Accés bloqué!")
                if self.get_tent()==3:
                    print("!Compte bloqué!")
                    break
                mdp=input("mot de passe: ")
        
        

    def changer_mot_de_passe(self,a_mdp,n_mdp):
        if a_mdp==self.get_mdp():
            if len(n_mdp)>=6:
                self.set_mdp(n_mdp)
                print("mot de passe changé!")
            else:
                print("mot de passe: au moins 6 characters..")
        else:
            print("ancien mot de passe incorrect!")
        
    def affiche_compte(self):
        print(f'compte: {self.id} - Nom: {self.nom} - Tentatives: {self.__tentative}')

    def del_compte(self):
        del self
        print("Compte supprimé!")
