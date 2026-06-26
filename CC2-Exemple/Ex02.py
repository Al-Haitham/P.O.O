from collections import defaultdict,Counter


machines = [
("PC01", ["TCP","HTTP","SSH"]),
("PC02", ["TCP","FTP"]),
("PC03", ["HTTP","DNS"]),
("PC04", ["TCP","HTTP","DNS"]),
("PC05", ["SSH","FTP"])
]

#Q01
d={}
for p in machines:
    d[p[0]]=list(p[1])
print(d)

#Q02
protocols=set()
for pc in machines:
    for pr in pc[1]:
        protocols.add(pr)
print(protocols)

dbp=defaultdict(list)
for prt in protocols:
    for pc,prts in d.items():
        if prt in prts:
            dbp[prt].append(pc)
print(dbp)

#Q03
print("Les protocoles utilisés par une seule machine:")
for prt,mch in dbp.items():
    if len(mch)==2:
        print(prt,end="\n")

#Q04
pcom=defaultdict(list)
for i in range(len(machines)-1):
    for j in range(i+1,len(machines)):
        if len(set(machines[i][1]) & set(machines[j][1]))>=1:
            pcom[machines[i][0]].append(machines[j][0])
print(pcom)


#Q05
dbpc={}
for p,c in dbp.items():
    dbpc[p]=len(c)
    
cMax=max(dbpc.values())
print(cMax)
maxPt=[p for p,mc in dbpc.items() if mc==cMax]
print(maxPt)
if len(maxPt)==1:
    print(f"Le protocole le plus utilisé est : {maxPt} ({cMax} machines)")
else:
    print(f"Les protocoles les plus utilisés sont : {','.join(maxPt)} (chaque utilisé par {cMax} machines)")


#Q06
matrix=[]
for i in machines:
    ligne=[]
    for j in machines:
        if set(i[1])==set(j[1]):
            ligne.append(' - ')
        else:
            com=set(i[1]) & set(j[1])
            ligne.append(len(com))
    matrix.append(ligne)

for l in matrix:
    print(l)

#Q07
currentPR=""
currentPC=""
maxC=0
pair=""
for l in range(len(matrix)):
    currentPR=machines[l][0]
    for p in range(len(matrix[l])):
        currentPC=machines[p][0]
        if matrix[l][p]==' - ':
            pass
        elif matrix[l][p]>maxC:
            maxC=matrix[l][p]
            pair=f"{currentPR} - {currentPC}"
print(pair,maxC,sep=" /",end=" machines\n")


#Q08
