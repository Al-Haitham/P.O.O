from src.etudiant import etudiant

e=etudiant(0,"haitam",22,17)
e.set_EtdAge(23)
print(e.get_EtdAge())
print(etudiant.affiche_Etd(e))