def f(a,n):
    if n%2==0:
        return (a**2)**(n//2)
    else:
        return a*a**(n-1)
a=int(input())
n=int(input())
print(f(a,n))
