n=int(input('n= '))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum-=i
        if i!=n:
            print(-i,'+ ',end='')
        else:
            print(-i,end='')
    else:
        sum+=i
        if i!=n:
            print(i,'+ ',end='')
        else:
            print(i,end='')
print('=',sum)
    