#Methode1
n=int(input('n='))
'''if n==n[::-1]:
    print('Palindrome')
else:
    print('Pas Palindrome')'''

#Methode2
n0=n
n1=0

while n0!=0:
    n1=n1*10+n0%10
    n0=n0//10
if n1==n:
    print('Palindrome')
else:
    print('Pas palindrome')