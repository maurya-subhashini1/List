num=int(input("enter the number:"))
a=0
b=[]
i=1
while i<num:
    if(num%i)==0:
        b.append(i)
        a=a+i
    i=i+1
print(b)
if a==num:
    print(num,"is perfect number") 
else:
    print(num,"is not perfect number")     
        