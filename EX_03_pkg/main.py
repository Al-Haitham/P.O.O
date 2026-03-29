from src.Rect import rectangle

#Instanciation
y=int(input("saisir la largeur: "))
x=int(input("saisir la longueur: "))
rect1=rectangle(y,x)

#print(rectangle.__doc__)
print(rect1.perimetre())
print(rect1.surface())