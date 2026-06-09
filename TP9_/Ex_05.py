from collections import deque

mot="radar"
d=deque(mot)

#Q1
palindrome=True

while len(d) > 1:
    if d.popleft()!=d.pop():
        palindrome=False
        break

print(palindrome)