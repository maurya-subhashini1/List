number=[50,20,30,23,40,56,12,5,10,7]
i=0
c=0
k=[]
while i<len(number):
    if number[i]>=20 and number[i]<=40:
        k.append(number[i])
        c=c+1
    i=i+1
print(k)
print(c)     
