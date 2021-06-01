i=10
s=[]
while i>0:
    num=int(input("enter the number"))
    s.append(num)
    i=i-1
user=int(input("enter the number"))
i=9
count=0
while i>0:
    if user==s[i]:
        print("yes")
        count=count+1
        i=i+1
if count==0:
    print("no")
if user in s:
    print("yes")
else:
    print("no")
