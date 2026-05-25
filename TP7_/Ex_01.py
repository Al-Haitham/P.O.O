commandes = [
            (1, "Ali", 250),
            (2, "Sara", 120),
            (3, "Ali", 300),
            (4, "Lina", 80),
            (5, "Sara", 220),
            (6, "Omar", 150)
            ]
#Q1
for c in commandes:
    print(f"Commande {c[0]} - {c[1]} - {c[2]} DH")

#Q2
Cs200=[c for c in commandes if c[2]>200]
print(Cs200)

#Q3
ClsR=[c[1] for c in commandes]
print(set(ClsR))

#Q4
sum=sum([c[2] for c in commandes])
print(f"Montant totale: {sum}")

#Q5
moy=sum/len(commandes)
print(f"Montant moyenne: {sum/len(commandes):.2f}")

#Q6 w/o max()
mMax1=0
cMax1=""
for c in commandes:
    if c[2]>mMax1:
        mMax1=c[2]
        cMax1=c
print(f"la commande {cMax1} avec une montant max: {mMax1} DH")

#Q6 w/ max()
mMax2=max([c[2] for c in commandes])
cMax2=[c for c in commandes if c[2]==mMax2]
print(f"la commande {cMax2} avec une montant max: {mMax2} DH")

#Q7
totals={}
for i,cl,mt in commandes:
    if cl not in totals:
        totals[cl]=0
    totals[cl]+=mt
print(totals)
for k,v in totals.items():
    print(f"{k}: {v}")

#Q8
pDep=[f"{k} depensé {v} DH" for k,v in totals.items() if v==max([v for k,v in totals.items()])]
print(pDep)

#Q9
commandes.append((7,'Nora',100))

#Q10
for i in range(len(commandes)-1,1,-1):
    if commandes[i][2]<100:
        commandes.pop(i)
print(commandes)

#Q11
nList=[c for c in commandes if c[2]>moy]

#Q12
nivList=[(c[0],c[1],"Elvé") if c[2]>=200 else (c[0],c[1],"Faible") for c in commandes]
print(nivList)
