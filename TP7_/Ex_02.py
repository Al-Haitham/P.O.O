#Q1
L=[0,1,2,3,4,5,6,7,8,9,10]

L1=[i*2 for i in L]
print(L1)
L2=[[i,i] for i in L]
print(L2)
L3=[i for i in L for _ in range(2)]
print(L3)
L4=[i for i in L +[i for i in L]]
print(L4)
L5=[i for i in L for _ in range(i)]
print(L5)

#Q2
Li1= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Li2 = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août","Septembre", "Octobre","Novembre", "Décembre"]

Li3=[[j,i] for i,j in zip(Li1,Li2)]
print(Li3)
