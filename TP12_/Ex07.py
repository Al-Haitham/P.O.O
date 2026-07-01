import re

mots_de_passe = [
"Azerty123",
"python",
"ADMIN2025",
"Test@123",
"abc123",
"SecurePass99"
]

pws_str=" ".join(mots_de_passe)
print(pws_str)

pw_1dl=re.findall(r"\b\S*\d\S*\b",pws_str)
print(pw_1dl)

pw_1Majl=re.findall(r"\b\S*[A-Z]+\S*\b",pws_str)
print(pw_1Majl)

pw_valide=re.findall(r"\b(?=\S*[A-Z])(?=\S*\d)\S{8,}\b",pws_str)
print(f"Nombre des mots de passe validés: {len(pw_valide)}\n{pw_valide}")