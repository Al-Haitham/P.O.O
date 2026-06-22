import pandas as pd
import os

os.chdir("/home/xy-haitam/Documents/GitHub/P.O.O/TP10_")


etd=pd.read_csv("etudiants.csv",sep=";")
print("Q--")
print(etd)
print("Q--")
print(etd.head(3))
print("Q--")
print(etd[["nom"]])
print("Q--")
print(etd[["nom","note"]])
print("Q--")
etd["admis"]=etd["note"]>=10
print("Q--")
etd.loc[etd["nom"]=="Omar","note"]=12
print("Q--")
etd.sort_values(by="note",ascending=False)
print(etd)
print("Q--")
moyNote=etd["note"].mean()
minNote=etd["note"].min()
maxNote=etd["note"].max()
print(moyNote,maxNote,minNote,sep=" - ")
print("Q--")
etd.to_csv("resultat.csv",index=True)
print("Q--")
def rechercher_etudiant(etd,nom):
    exist=False
    for i,ed in etd.iterrows():
        if ed["nom"]==nom:
            print(ed["note"])
            exist=True
            break
    if exist==False:
        print("Étudiant introuvable!")
        

print("Q--")
nom=input("Saisir un nom a rechercher: ")
rechercher_etudiant(etd,nom)