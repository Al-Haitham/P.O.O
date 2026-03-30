from src.MyClasses import Cercle
import math

#Instanciation
c1=Cercle(7,3,math.sqrt(8))
print(c1.surface())
print(c1.perimetre())
print(c1.testAppartenance(5,2))