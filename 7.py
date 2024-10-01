def IsPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 1
    return 0
x=int(input())
if IsPrime(x)==0:
    print("Yes")
else:
    print("No")
