from collections import defaultdict

liaisons=[("A","B"),("A","C"),("B","D"),("C","D"),("D","E")]

graphe=defaultdict(list)

#Q1
for a, b in liaisons:
    graphe[a].append(b)
    graphe[b].append(a)

print(dict(graphe))

#Q2
print(graphe["A"])

#Q3
def chemin(graph, debut, fin, visites=None):
    if visites is None:
        visites=set()

    if debut==fin:
        return True

    visites.add(debut)

    for voisin in graph[debut]:
        if voisin not in visites:
            if chemin(graph, voisin, fin, visites):
                return True

    return False

print(chemin(graphe,"A","E"))