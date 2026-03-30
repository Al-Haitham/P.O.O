class livre:
    """
    Documentation: Classe livre
    
    Représente un livre dans une bibliothèque.

    Attributs :
    ----------
    biblio : str
        Nom de la bibliothèque (attribut de classe).
    LivId : int
        Identifiant du livre.
    LivTitre : str
        Titre du livre.
    LivAut : str
        Auteur du livre.
    LivNbPg : int
        Nombre de pages.
    _LivPrx : float
        Prix du livre (attribut privé).

    Méthodes :
    ----------
    __init__(titre, auteur, pages, prix, id=0)
        Initialise un livre avec ses informations.

    get_LivPrx()
        Retourne le prix du livre.

    set_LivPrx(prix)
        Modifie le prix du livre si la valeur est positive.

    affiche_Livre()
        Affiche les informations du livre.

    moy_prx_page()
        Calcule le prix moyen par page.

    __str__()
        Retourne une représentation du livre sous forme de chaîne.

    biblio_Nom(biblio)
        Permet de modifier le nom de la bibliothèque.
    """
    biblio="BiblioTech"
    def __init__(self,id,titre,auteur,pages,prix):
        self.LivId=id
        self.LivTitre=titre
        self.LivAut=auteur
        self.LivNbPg=pages
        self._LivPrx=prix
    
    def get_LivPrx(self):
        return self._LivPrx
    
    def set_LivPrx(self,prix):
        if prix>=0:
            self._LivPrx=prix
        else:
            print(f"{prix} est un valeur incorrect!")
    
    def affiche_Livre(self):
        print(f"++++++++++++++++++++++++++++\nid: {self.LivId}\nTitre: {self.LivTitre}\nAuteur: {self.LivAut}\nPages: {self.LivNbPg}\nPrix: {self.get_LivPrx()}")
    
    def moy_prx_page(self):
        moyP=self.get_LivPrx()/self.LivNbPg
        print("Prix moyenne par page: ",end="")
        return moyP
    
    def __str__(self):
        print(f"id: {self.LivId}\nTitre: {self.LivTitre}\nAuteur: {self.LivAut}\nPages: {self.LivNbPg}\nPrix: {self.get_LivPrx()}")

    @classmethod
    def biblio_Nom(cls,biblNom):
        try:
            cls.biblio=biblNom
            print("Nom du biblioteque changé avec succés!")
        except Exception as e:
            print("Erreur de changement de nom: ",e)