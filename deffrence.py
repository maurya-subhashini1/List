# Q: Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which 
# numbers are not present in the second array.


a = [1,2,3,4,5,6]
b = [2,3,1,0,6,7]
i=0
x=[]
while i<len(a):
    c=a[i]
    if c not in b:
        x.append(c)
    i=i+1
print(x)
