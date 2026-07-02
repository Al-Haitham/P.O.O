import re
from collections import defaultdict

logs = """
2026-01-10;Ali;SUCCESS
2026-01-10;Ali;FAILED
2026-01-10;Ali;FAILED
2026-01-10;Ali;FAILED
2026-01-10;Sara;SUCCESS
2026-01-10;Omar;FAILED
2026-01-10;Omar;FAILED
"""

usrSt=re.sub(";"," ",logs)
print(usrSt)

users=re.findall(r"\b(?P<utilisateur>[A-Z][a-z]+?) (?P<status>[A-Z]+\b)",usrSt)
print(users)

cu=defaultdict(int)
for u,s in users:
    
    if s=="FAILED":
        cu[u]+=1
    else:
        cu[u]+=0
print(cu)


for u,cs in cu.items():
    if cs>=3:
        print(u)

