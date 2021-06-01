# Make a list by taking 10 input from user.
#  Now delete all repeated elements of the list.

element=[1,2,3,2,1,3,12,12,32]
i=0
l=[]
while i<len(element):
    a=element[i]
    if a not in l:
        l.append(a)
    i=i+1
print(l)

