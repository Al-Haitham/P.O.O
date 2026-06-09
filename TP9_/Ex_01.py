from collections import Counter

votes=["Ali","Sara","Ali","Omar","Sara","Ali","Omar","Sara"]

c=Counter(votes)

#Q1
print(c.most_common(1))

#Q2
max_votes=max(c.values())
egalite=sum(1 for v in c.values() if v==max_votes)>1
print(egalite)

#Q3
print(c.most_common())