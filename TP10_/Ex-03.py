import pandas as pd
import numpy as np
import os

os.chdir("/home/xy-haitam/Documents/GitHub/P.O.O/TP10_")
df=pd.read_csv("performances.csv",sep=",")
df["score_final"]=(df["precision"]+df["vitesse"])/2
df["niveau"]=np.select([(df["score_final"]>=85),(df["score_final"]<85) & (df["score_final"]>=70),(df["score_final"]<70)],
                       ["Expert","Intermédiaire","Débutant"],default="")
for i,e in df.iterrows():
    if e["niveau"]=="Expert":
        print(f"{e}\n")

df=df.sort_values(by="score_final",ascending=False)

df.to_csv("resultats_final.csv")