import re
from collections import defaultdict

trafic = """
192.168.1.1 -> 10.0.0.5
192.168.1.1 -> 10.0.0.8
192.168.1.2 -> 10.0.0.5
192.168.1.3 -> 10.0.0.5
192.168.1.1 -> 10.0.0.5
"""

pattern=r"(?:1[0-9]{2}|2[0-4][0-9]|25[0-5]|[0-9]|[0-9]{2})"

res=re.findall(rf"\b{pattern}(?:\.{pattern}){{3}}\s*->\s*{pattern}(?:\.{pattern}){{3}}", trafic)
print(res)

resIp=[]
for i in res:
    resIp.append(tuple(re.split(r"\s*->\s*",i)))
print(resIp)

dc=defaultdict(list)
for s,d in resIp:
    dc[s].append(d)

print(dc)
r={k:len(v) for k,v in dc.items()}
print(r)

print(max(r))



dcd=defaultdict(list)
for s,d in resIp:
    dcd[d].append(s)

print(dcd)
rd={k:len(v) for k,v in dcd.items()}
print(rd)

print(max(rd))