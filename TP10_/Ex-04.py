import os
os.chdir("/home/xy-haitam/Documents/GitHub/P.O.O/TP10_")

if os.path.exists("TP_Python")==False and os.path.exists("Logs")==False:
    os.makedirs("TP_Python/Logs")
    
print(os.path.exists("TP_Python"))
print(os.getcwd())
os.chdir("TP_Python")
print(os.listdir())
print(os.path.isdir("Logs"))
f=open("test.txt","w")
os.rename("test.txt","resultat.txt")