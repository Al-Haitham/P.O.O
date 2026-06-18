from collections import defaultdict

relations=[
    ("Ali","Sara"),
    ("Sara","Omar"),
    ("--","Yasmine"),
    ("Omar","Amine")
]

reseau=defaultdict(set)

#Q1
for a, b in relations:
    if a !="--":
        reseau[a].add(b)
    if b !="--":
        reseau[b].add(a)

print(dict(reseau))

#Q2
print(reseau["Ali"])

#Q3
print(reseau["Ali"] & reseau["Sara"])

#Q4
print(reseau["Yasmine"])
isolés=[p for p, amis in reseau.items() if "--" in amis]
print(isolés)