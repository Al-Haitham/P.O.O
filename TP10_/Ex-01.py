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

