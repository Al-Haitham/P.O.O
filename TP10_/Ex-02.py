from collections import defaultdict
import os

os.chdir("/home/xy-haitam/Documents/GitHub/P.O.O/TP10_")

f=open("matchs.txt","r")
vect=defaultdict(int)
for l in f:
    elt=l.strip().split()
    
    v=""
    if len(elt)!=4:
        print("Nombre des elements invalide!")
        continue
    j1,j2,s1,s2=elt[0],elt[1],int(elt[2]),int(elt[3])
    vect[j1]

    if s1>s2:
        vect[j1]+=1
        v=j1
        print(f"{j1} vs {j2} est le gagnant est: {v}")
    if s2>s1:
        vect[j2]+=1
        v=j2
        print(f"{j1} vs {j2} est le gagnant est: {v}")
    else:
        vect[j1]+=0
        vect[j2]+=0
f.close()

print(vect)
with open("classement.txt","w" ) as c:
    c.write("Joueur - Score\n-------+-------\n")
    for j,s in vect.items():
        c.write(f"{j} - {s}\n")