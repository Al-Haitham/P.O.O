#Q01
L=[10,20,30,40,50]
L[1:4]=[100,200]
print(L)

"""
le resultat sera:
[10,100,200,50]

le role de L[1:4]=[100,200] est:
L[1:4]: slice du position 1 jusqu'a 3 (4-1) 
=[100,200]: remplace le slice par les deux elements 100 et 200 
"""

#Q02
"""
On va utiliser un dictionnaire, parce que les matricules va etre les clé, et les notes sera stocké dans les valeurs
"""

#Q03
A={"Python","Java","C++"}
B={"Python","JavaScript","C++"}

print(A & B)
#resultat: {'Python','C++'}

#Q04
#Pickle: car il garde la meme forme

