a=int(input('a='))
b=int(input('b='))
c=int(input('c='))

if a>b and a>c:
    print(f'a={a} est Dominant')
elif b>a and b>c:
    print(f'b={b} est Dominant')
elif c>a and c>b:
    print(f'c={c} est Dominant')
else:
    print('équilibre')
