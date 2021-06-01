# i=10
# a=[]
# sum=0
# while i>0:
#     num=int(input("enter the number"))
#     sum=sum+num
#     a.append(sum)
#     i=i-1
# print(a)

a=[[1,2,3],[4,5,6]]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print (a[i][j])
        j=j+1
    i=i+1
