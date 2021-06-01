i=10
a=[]
b=[]
c=[]
d=[]
e=[]
while i>0:
    num=int(input("enter the number"))
    if num==0:
        a.append(num)
    if num%2==0:
        b.append(num)
    else:
        c.append(num)
        if num>0:
            d.append(num)
        else:
            e.append(num)
    i=i-1
print("zeero",a) 
print("even",b)
print("odd",c)
print("postive",d)
print("negative",e)       


