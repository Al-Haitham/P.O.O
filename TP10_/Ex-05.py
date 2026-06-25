import os

os.chdir("/home/xy-haitam/Documents/GitHub/P.O.O/TP10_")

if os.path.exists("MonDossier")==False:
    os.mkdir("MonDossier")
os.chdir("MonDossier")
for fi in range(3):
    if os.path.exists(f"rep{fi}")==False:
        os.mkdir(f"rep{fi}")
        os.chdir(f"rep{fi}")
        f=open(f"mariere{fi}.txt","w")
        f.write(f"c est un nouveau fichier matiere{fi} !")
        f.close()
        os.chdir("/home/xy-haitam/Documents/GitHub/P.O.O/TP10_/MonDossier")
os.chdir("")
f=open("matiere0","r")
print(f)