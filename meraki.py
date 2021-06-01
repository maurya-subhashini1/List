
# Write a program to print sum, average of all numbers, smallest and 
# largest element of a list.

number=[1,2,12,34,32,23,14,51,38]
i=0
k=[]
sum=0
avg=0
a=number[0]
b=number[0]
while i<len(number):
    sum=sum+number[i]
    k.append(sum)
    avg=sum//len(k)
    sum=sum+1
    if number[i]>a:
        a=number[i]
    elif number[i]<b:
        b=number[i]
    i=i+1
print("sum",sum,"avrege",avg,"largest",a,"smallest",b)





