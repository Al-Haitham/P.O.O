import math
class Cercle:

    def __init__(self,a,b,r):
        self.a=a
        self.b=b
        self.rayon=r
    
    def surface(self):
        s=math.pi*(self.rayon)**2
        print(f"la surface de la cercle {self} est: ",end="")
        return s
    
    def perimetre(self):
        p=2*math.pi*self.rayon
        return p

    def testAppartenance(self,x,y):
        distance=math.sqrt((x-self.a)**2+(y-self.b)**2)
        if distance==self.rayon:
            return f"Le point A({x},{y}) appartient au cercle"
        else:
            return f"Le point A({x},{y}) n'appartient pas au cercle"