a=[1,2,3,4,5,6,7,8,9,10]
n=int(input("enter a number"))
i=0
sum=0
while i<len(a[:n]):
    num=a[i]
    sum=sum+num 
    i=i+1
print(sum)
j=n
s=0
while j<len(a):
    num1=a[j]
    s=s+num1
    j=j+1
print(s)
print("the multiplication of sum of the number list",sum*s)




