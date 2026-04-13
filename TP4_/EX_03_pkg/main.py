from src.MyClasses import rectangle, parallepipede

#Instanciation
long=int(input("entrer la longueur: "))
larg=int(input("entrer la largeur: "))
haut=int(input("entrer la hauteur: "))
r1=rectangle(long,larg)
r1.draw()
print(r1.perimetre())
print(r1.surface())
haut=int(input("entrer la hauteur: "))
p1=parallepipede(long,larg,haut)
print(p1.volume())