places=["delhi","gujrat","rajasthan","punjab","keral"]
i=0
a=[]
while i<len(places):
    k=places[i]
    k=places[len(places)-i-1]
    a.append(k)
    i=i+1
print(a)        


