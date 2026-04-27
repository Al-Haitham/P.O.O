from abc import ABC, abstractmethod
class Vehicule(ABC):
    def __init__(self,marque,vitesse):
        self.marque=marque
        self.vitesse=vitesse

    @abstractmethod
    def demarrer(self):
        print("la vehicule est demarré!")
    @abstractmethod
    def calculer_vitesse(self):
        return self.vitesse
    
    def afficher_infos(self):
        print(f"la marque: {self.marque} - {self.calculer_vitesse()} Km/h")
    
class voiture(Vehicule):
    def demarrer(self):
        print("la voiture est demarré!")
    def calculer_vitesse(self):
        return self.vitesse
    
class moto(Vehicule):
    def demarrer(self):
        print("la moto est demarré!")
    def calculer_vitesse(self):
        return self.vitesse+10