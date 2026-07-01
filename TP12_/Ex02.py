import re

phrase = "La facture N°4587 a été validée."

ereNb=re.search(r"\d+",phrase)
print(ereNb.group())
print(ereNb.start())
print(ereNb.end())

