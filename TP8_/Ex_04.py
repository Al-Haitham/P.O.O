from collections import Counter

texte="programmation python"

c1=Counter(texte)
print("-----")
print(c1)
print("-----")
print(c1.most_common(1))
print("-----")
print(c1.most_common(3))
print("-----")
for lettre in sorted(c1):
    print(lettre, c1[lettre])
print("-----")
print(c1["p"])
print("-----")
print(c1["z"])
print("-----")
c2=Counter("python")

c1.subtract(c2)

print(c1)