from collections import deque

joueurs=deque(["A","B","C","D","E","F"])

"""
c=0
while len(joueurs)>1:
    c=(c+2)%len(joueurs)
    joueurs.rotate(-c)
    print(joueurs)
    eliminated = joueurs.popleft()  
print(f"Survivor: {joueurs}")
"""
c=0
while len(joueurs)>1:
    for i in len(joueurs):
        c+=1
        if c==3:
            joueurs.