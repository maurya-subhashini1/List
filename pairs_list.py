number = 30
n = [10, 11, 20, 13, 14, 17, 18, 19] 
i=0
c=[]
while i<len(n):
    a=0
    while a<len(n):
        if n[i]+n[a]==30:
            b=([n[i],n[a]])
            c.append(b)
        a=a+1
    i=i+1
print(c)
