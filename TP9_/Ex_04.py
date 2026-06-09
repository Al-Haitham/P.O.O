from collections import defaultdict

relations=[
    ("Ali","Sara"),
    ("Sara","Omar"),
    ("Ali","Yasmine"),
    ("Omar","Amine")
]

reseau=defaultdict(set)

#Q1
for a, b in relations:
    reseau[a].add(b)
    reseau[b].add(a)

print(dict(reseau))

#Q2
print(reseau["Ali"])

#Q3
print(reseau["Ali"] & reseau["Sara"])

#Q4
isolés=[p for p, amis in reseau.items() if len(amis)==0]
print(isolés)