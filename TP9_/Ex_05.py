from collections import deque

mot="radar"
d=deque(mot)

#Q1
p="Pas palindrome .."
while len(d) > 1:
    if d.popleft()==d.pop():
        p="Palindrome!"

print(p)