import re

texte = "Python est simple et Python est puissant"

print(re.sub("Python","Java",texte))
print(re.sub("Python","Java",texte,1))
print(re.sub(r"\s","_",texte))
