class rectangle:
    """
    Documentation: Classe rectangle

    Represent un rectangle avec une largeur et une longueur
    ##########
    Attributs:
    RectLarg: int
    Largeur du rectangle
    RectLong: int
    Longueur du rectangle
    ##########
    Méthodes:
    __init__(y, x)
    Initialise un rectangle avec une largeur (y) et une longueur (x)
    Vérifie que les valeurs sont positives et affiche une représentation du rectangle avec des "*"

    perimetre()
    Calcule et retourne le périmètre du rectangle

    surface()
    Calcule et retourne la surface du rectangle
    """
    def __init__(self,y,x):
        try:
            if y>0 and x>0:
                self.RectLarg=y
                self.RectLong=x
                for i in range(0,self.RectLarg):
                    print("+ "*self.RectLong)
        except Exception as e:
            print("erreur: ",e)
        

    def perimetre(self):
        p=2*self.RectLarg+2*self.RectLong
        print(f"Le perimétre de rectangle {self} est: ",end="")
        return p

    def surface(self):
        s=self.RectLarg*self.RectLong
        print(f"La surface du rectangle {self} est: ",end="")
        return s
