elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
h=[]
n=[]
while i<len(elements):
    a=elements[i]
    if a%2==0:
        h.append(a)
    else:
        n.append(a)
    i=i+1
print("even number=",h,"odd number=",n)
