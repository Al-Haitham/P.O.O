class Chambre:
    nb_chambers=0
    def __init__(self, numero=0,prix_nuit=0.0):
        self.__numero=numero
        self.__prix_nuit=prix_nuit
        Chambre.nb_chambers+=1

    def get_numero(self):
        return self.__numero
    def set_numero(self,numero):
        self.__numero=numero
    def get_prix_nuit(self):
        return self.__prix_nuit
    def set_prix_nuit(self,prix_nuit):
        self.__prix_nuit=prix_nuit

    def calculer_prix_nuit(self):
        return self.__prix_nuit
    
    def __str__(self):
        print(f"Numero: ${self.get_numero} \nType de Chambre: ${type(self).__name__} \nPrix: ${self.calculer_prix_nuit}")


class ChambreStandard(Chambre):
    def __init__(self,petit_dejeuner_inclus, numero=0, prix_nuit=0.0):
        super().__init__(numero, prix_nuit)
        self.__petit_dejeuner_inclus=petit_dejeuner_inclus

    def get_petit_dejeuner_inclus(self):
        return self.__petit_dejeuner_inclus
    def set_petit_dejeuner_inclus(self,petit_dejeuner_inclus):
        self.__petit_dejeuner_inclus=petit_dejeuner_inclus

    def calculer_prix_nuit(self):
        if self.__petit_dejeuner_inclus==True:
            return self.get_prix_nuit()+50
        else:
            return self.get_prix_nuit()
    
class Suite(Chambre):
    def __init__(self,nb_pieces, numero=0, prix_nuit=0.0):
        super().__init__( numero, prix_nuit)
        self.__nb_pieces=nb_pieces
    
    def get_nb_pieces(self):
        return self.__nb_pieces
    def set_nb_pieces(self,nb_pieces):
        if self.__nb_pieces>0:
            self.__nb_pieces=nb_pieces
        else:
            print("nmbre des pieces de suite invalid!")

    def calculer_prix_nuit(self):
        return self.get_prix_unit+self.__nb_pieces*200
    
class Reservation:
    
    def __init__(self,liste_chambre=[]):
        self.__liste_chambre=liste_chambre
    
    def ajouter_chambre(self,Chambre):
        self.__liste_chambre.append(Chambre)
    
    def calculer_cout_total(self,nb_nuits):
        sumCout=0
        for c in self.liste_chambre:
            sumCout+=c.calculer_prix_nuit()*nb_nuits
        return sumCout
    def __str__()   #return sum([c.calculer_prix_nuit()*nb_nuits for c in self.liste_chambre])

    def afficher_details(self,nb_nuits):
        print(f"nombre des chambre: {len(self.__liste_chambre)} - le Cout totale: {self.calculer_cout_total}")
    
    def __add__(chambre):
        if not isinstance(chambre,Chambre):
            raise TypeError("")

    def __len__(self):
        return len(self.__liste_chambre)
    
    