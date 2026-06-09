from functools import reduce
from operator import xor

L=[5,8,5,8,5,8,5]

#Q1
print(reduce(xor, L))