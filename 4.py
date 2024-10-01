f2=int(input())
maxx=0
k=1
f1=0
while f2!=0:
    if f1==f2:
        k=k+1
        maxx=k
    else:
        k=1
    f1=f2
    f2=int(input())
print(maxx)
    
