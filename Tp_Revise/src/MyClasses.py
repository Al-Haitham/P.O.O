from abc import ABC, abstractmethod
#Q01
class Vehicule(ABC):
    def __init__(self,immatricule,marque,annee,prixAchat):
        self.__immatricule=immatricule
        self.__marque=marque
        self.__annee=annee
        self.__prixAchat=prixAchat
    #Q02
    @abstractmethod
    def calculerCoutExploitation(self):
        pass

    def get_immatricule(self):
        return self.__immatricule
    def get_marque(self):
        return self.__marque
    def get_annee(self):
        return self.__annee
    
    #Q05
    @property
    def prixAchat(self):
        return self.__prixAchat
    
    @prixAchat.setter
    def prixAchat(self,prixAchat_New):
        self.prixAchat=prixAchat_New

    
#Q03
class Bus(Vehicule):
    #Q04
    def calculerCoutExploitation(self):
        print("Le coût annuel d'exploitation est:")
        return self.get_prixAchat * 0.08 + 30000
    #Q06
    def __str__(self):
        return f"immatricule de Bus:{self.get_immatricule}\nMarque: {self.get_marque}\nAnnee:{self.get_annee}\nPrix d'achat: {self.prixAchat}\nCoût annuel:{self.calculerCoutExploitation}"
#Q03
class Taxi(Vehicule):
    #Q04
    def calculerCoutExploitation(self):
        print("Le coût annuel d'exploitation est:")
        return self.get_prixAchat * 0.05 + 12000
    #Q06
    def __str__(self):
        return f"immatricule de Taxi:{self.get_immatricule}\nMarque: {self.get_marque}\nAnnee:{self.get_annee}\nPrix d'achat: {self.prixAchat}\nCoût annuel:{self.calculerCoutExploitation}"

#Q07 
class AgenceTransport():
    def __init__(self):
        self.vehicules=[]

    #Q08
    def add_vehicule(self,veh):
        self.vehicules.append(veh)
        print("vehicule ajouté avec success!")
    
    def delete_vehicule(self,imma):
        self.vehicules=[v for v in self.vehicules if v.get_immatricule!=imma]
        print("vehicule supprimé avec success!")
    
    def rech_vehicule(self,imma):
        for v in self.vehicules:
            if v.get_immatricule==imma:
                return v
        return None