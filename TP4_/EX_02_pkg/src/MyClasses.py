class rectangle:
    def __init__(self,longueur,largeur):
        try:
            if longueur>0 and largeur>0:
                self._largeur=largeur
                self._longueur=longueur
        except Exception as e:
            print("erreur: ",e)
    def draw(self):
        for i in range(0,self._largeur):
            print("+ "*self._longueur)

    def perimetre(self):
        print("le perimetre est : ")
        return 2*(self._longueur+self._largeur)

    def surface(self):
        print("la surface est : ")
        return self._longueur*self._largeur

    def get_longueur(self):
        return self._longueur
    def get_largeur(self):
        return self._largeur
    def set_longueur(self,longueur):
        self._longueur=longueur
    def set_largeur(self,largeur):
        self._largeur=largeur
    
class parallepipede(rectangle):
    def __init__(self,longueur,largeur,hauteur):
        super().__init__(longueur,largeur)
        self._hauteur=hauteur

    def get_hauteur(self):
        return self._hauteur
    def set_hauteur(self,hauteur):
        self._hauteur=hauteur

    def volume(self):
        print("le volume est : ")
        return self.get_longueur()*self.get_largeur()*self.get_hauteur()
    