from abc import ABC,abstractmethod
class Correcteur(ABC):
    def __init__(self,reponses_etudiant,corrections):
        self.reponses_etudiant=reponses_etudiant
        self.corrections=corrections

    @abstractmethod
    def est_valide(self):
        pass
    
    @abstractmethod
    def calculer_score(self):
        pass

    @abstractmethod
    def afficher_resultat(self):
        pass

class CorrcteurQCM(Correcteur):
    def est_valide(self):
        if len(self.reponses_etudiant)!=len(self.corrections) and (len([True for r in self.reponses_etudiant if r in self.corrections])==len(self.corrections)):
            return False
        for r in self.reponses_etudiant:
            if r not in set(self.corrections):
                return False
    def calculer_score(self):
        score=0
        if self.est_valide():
            for r,c in zip(self.reponses_etudiant,self.corrections):
                if r==c:
                    score+=1
                else:
                    score-=0.25
            return score

    def afficher_resultat(self):
        return self.calculer_score