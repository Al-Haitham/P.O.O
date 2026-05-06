from abc import ABC, abstractmethod

class Forme(ABC):
    def __init__(self,nom):
        self.nom=nom
    
    @abstractmethod
    def calculer_aire():
        pass
    @abstractmethod
    def dessiner():
        pass

class Rectangle:
    def __init__(self,longueur,largeur):
        self.longueur=longueur
        self.largeur=largeur
    def calculer_aire(self):
        return self.longueur*self.largeur
    def dessiner(self):
        for y in range(0,self.longueur):
            for x in range(0,self.largeur):
                print("+",end="")
            print()

class Triangle:
    def __init__(self,hauteur,base):
        self.hauteur=hauteur
        self.base=base
    def calculer_aire(self):
        return (self.hauteur*self.base)/2
    def dessiner(self):
        for b in range(0,self.hauteur):
            print(" "*(self.hauteur-b-1),"+"*(2*b+1))