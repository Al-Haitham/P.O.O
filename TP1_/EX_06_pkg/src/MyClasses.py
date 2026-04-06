class Calcul:

    def __init__(self):
        pass

    def Factorielle(self,n):
        f=1
        if n==0:
            print(f"{n}!= ",end="")
            return 1
        else:
            for i in range(1,n+1):
                f*=i
            print(f"{n}!= ",end="")
            return f

    def Somme(self,n):
        s=0
        for i in range(1,n+1):
            s+=i
        return s
        
    def tableMult(self,n):
        if n<0:
            print(f"{n} est negative")
        else:
            for i in range(1,11):
                print(f"{i} x {n} = {i*n}")

    def allTablesMult(self):
        for i in range(1,11):
            self.tableMult(i)
            #print(f"-> table de {i}:")
            #for j in range(1,11):
                #print(f"{i} x {j} = {i*j}")
            print("")

    def listDiv(self,n):
        Ldiv=[]
        for i in range(1,n+1):
            if n%i==0:
                Ldiv.append(i)
        return Ldiv

    def listDivPrim(self,n):
        LdivPr=[]
        for d in self.listDiv(n):
            if len(self.listDiv(d))==2:
                LdivPr.append(d)
        return LdivPr
