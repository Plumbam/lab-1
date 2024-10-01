x=int(input())
maxx=0
i=0
while x!=0:
    if x>maxx:
        i=maxx
        maxx=x
    x=int(input())
print(i)
    
