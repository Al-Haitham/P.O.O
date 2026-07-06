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
    
    #Q04
    @abstractmethod
    def coutTotale(self):
        pass

    #Q05
    @property
    def prixAchat(self):
        return self.__prixAchat
    
    @prixAchat.setter
    def prixAchat(self,prixAchat_New):
        self.prixAchat=prixAchat_New

    #Q10
    @abstractmethod
    def afficher(self):
        pass
    

    
#Q03
class Bus(Vehicule):
    #Q04
    def calculerCoutExploitation(self):
        print("Le coût annuel d'exploitation est:")
        return self.get_prixAchat * 0.08 + 30000
    #Q06
    def __str__(self):
        return f"immatricule de Bus:{self.get_immatricule}\nMarque: {self.get_marque}\nAnnee:{self.get_annee}\nPrix d'achat: {self.prixAchat}\nCoût annuel:{self.calculerCoutExploitation}"
    #Q10
    def afficher(self):
        return f"Bus: {self.get_immatricule} - {self.get_marque} - {self.get_annee} - {self.prixAchat}"
#Q03
class Taxi(Vehicule):
    #Q04
    def calculerCoutExploitation(self):
        print("Le coût annuel d'exploitation est:")
        return self.get_prixAchat * 0.05 + 12000
    #Q06
    def __str__(self):
        return f"immatricule de Taxi:{self.get_immatricule}\nMarque: {self.get_marque}\nAnnee:{self.get_annee}\nPrix d'achat: {self.prixAchat}\nCoût annuel:{self.calculerCoutExploitation}"
    #Q10
    def afficher(self):
        return f"Taxi: {self.get_immatricule} - {self.get_marque} - {self.get_annee} - {self.prixAchat}"
#Q07 
class AgenceTransport():
    def __init__(self):
        self.vehicules=[]

    #Q08
    def ajouterVehicule(self,veh):
        self.vehicules.append(veh)
        print("vehicule ajouté avec success!")
    
    def supprimerVehicule(self,imma):
        self.vehicules=[v for v in self.vehicules if v.get_immatricule!=imma]
        print("vehicule supprimé avec success!")
    
    def rechercherVehicule(self,imma):
        for v in self.vehicules:
            if v.get_immatricule==imma:
                return v
        return None
    
    #Q09
    def modifPrixAch(self,nPrix,imma):
        for v in self.vehicules:
            if v.get_immatricule==imma:
                if nPrix>0:
                    v.get_prixAchat=nPrix
                else:
                    print("Prix invalide !")
    
    #Q10
    def affciher_tous(self):
        for v in self.vehicules:
            print(v.afficher())
    
    #Q11
    def coutTotale(self):
        totale=0
        for v in self.vehicules:
            totale+=v.calculerCoutExploitation()
        return totale
    
    #Q12
    def plusElvCout(self):
        coutMax=0
        max=""
        for v in self.vehicules:
            if v.calculerCoutExploitation()>coutMax:
                coutMax=v.calculerCoutExploitation()
                max=v.afficher()
        return max
    
    #Q13
    def plusElvCout(self):
        coutMax=self.plusElvCout()
        max=""
        for v in self.vehicules:
            if v.calculerCoutExploitation()<coutMax:
                coutMax=v.calculerCoutExploitation()
                max=v.afficher()
        return max
    
    #Q14
    def coutMoy(self):
        return (self.coutTotale()/len(self.vehicules))

    #Q15
    def vPlusQueMoy(self):
        moy=self.coutMoy()
        vPlusQueMoy=[]
        for v in self.vehicules:
            if v.calculerCoutExploitation()>moy:
                vPlusQueMoy.append(v)
        return vPlusQueMoy
    
    #Q15
    def descSort(self):
        descSortList=[]
        listToSort=self.vehicules[:]
        max_v=listToSort
        sortedList=[]
        while listToSort!=[]:
            for v in listToSort:
                if v.calculerCoutExploitation()>max_v.calculerCoutExploitation():
                    max_v=v
            sortedList.append(max_v)
            listToSort.remove(max_v)
        return sortedList
                
