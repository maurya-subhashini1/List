a=[1,22,33,2,334,56,67,78,89,90,99]
i=0
d=a[0]
f=a[0]
while i<len(a):
    if a[i]>d:
        d=a[i]
    elif a[i]<f:
        f=a[i]
    i=i+1
print("smalst",f)