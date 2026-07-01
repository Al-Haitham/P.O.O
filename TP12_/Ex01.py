import re

texte = """
Ali a 22 ans.
Sara a 19 ans.
Omar a 31 ans.
Yasmine a 25 ans.
"""
ages=re.findall(r"\d{1,2}",texte)
print(ages)
prenoms=re.findall(r"[A-Z][a-z]{2,}",texte)
print(prenoms)
nbr2d=re.findall(r"\b\d{2}\b",texte)
print(nbr2d)
motMaj=re.findall(r"[A-Z][a-z]*",texte)
print(motMaj)
print(len(prenoms))
