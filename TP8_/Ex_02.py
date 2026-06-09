from collections import deque

file=deque()

file.append("Ali")
file.append("Sara")
file.append("Omar")

file.appendleft("Police")

print(file)

print(file.popleft())
print(file.pop())

print(file)

file.clear()

print(file)