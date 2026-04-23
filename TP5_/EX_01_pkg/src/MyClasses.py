class chaine:
    def __init__(self,chc):
        self.chaine_de_character=chc

    def afficher(self):
        return self.chaine_de_character
    
class phrase(chaine):
    def __init__(self,chc,lng):
        super().__init__(chc)
        self.langue=lng

    def afficher(self):
        return f"phrase: {super().afficher()}\n--langue: {self.langue}"
    
    def type(self):
        if self.chaine_de_character.endswith("."):
            return "Type: déclaratif"
        elif self.chaine_de_character.endswith("?"):
            return "Type: interrogatif"
        elif self.chaine_de_character.endswith("!"):
            return "Type: exclamatif"
        else:
            return "Auncun type declaré!"


    def longueurMot(self):
        motList=self.chaine_de_character[0:len(self.chaine_de_character)-1].split()
        max=len(motList[0])
        maxMot=motList[0]
        for i in range(len(motList)):
            if len(motList[i])>max:
                max=len(motList[i])
                maxMot=motList[i]
        return f"{maxMot} -> {max} mots"
    
