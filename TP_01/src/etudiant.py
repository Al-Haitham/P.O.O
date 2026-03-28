class etudiant:
    def __init__(self,id,nom,age,moy):
        self.EtdId=id
        self.EtdNom=nom
        self.__EtdAge=age
        self.EtdMoy=moy

    def get_EtdAge(self):
        return self.__age

    def set_EtdAge(self,age):
        if age>0:
            self.__EtdAge=age
        else:
            print("Valeur d'age incorrect!")
