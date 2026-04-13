class SalleCinema:
    def __init__(self,nom,capacite,pl_occup):
        self.nom=nom
        self.capacite=capacite
        self._places_occupe=pl_occup
    
    def reserver(self,nb_places):
        if nb_places<=self.capacite-self._places_occupe:
            print(f'Reservation accepté.\n{nb_places} places a bien reservé dans {self.nom}!')
            self._places_occupe+=nb_places
        else:
            print("Reservations refusé")

    def annuler(self,nb_places):
        if nb_places<=self._places_occupe:
            self._places_occupe-=nb_places
            print("Places annulé avec succes!")
        else:
            print("Places pas annulé!")
    
    def taux_remp(self):
        taux=self._places_occupe*100/self.capacite
        print("le taux de remplisage est : ")
        return taux
    
    def afficher(self):
        print(f"Salle cinema {self.nom}: \ncapacité: {self.capacite}\nplaces occupés: {self._places_occupe}")
        return self._places_occupe