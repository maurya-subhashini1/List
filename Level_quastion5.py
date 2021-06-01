
# Write a program to find the sum of all elements of a list.


number=[1,2,3,4,44,22,33,43,12]
i=0
sum=0
while i<len(number):
    a=number[i]
    sum=sum+a
    sum=sum+i
    i=i+1
print(sum)


