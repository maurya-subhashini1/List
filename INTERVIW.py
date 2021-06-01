

a=[1,2,3,4,5,6,7,8,9]
n=int(input("enter a number"))
i=-1
k=[]
while i<len(a):
    k.append(a[i])
    # print(a[i])
    if a[i]==n:
        break
    i=i-1
print(k)



# # a=[45,42,67,12,34,55,66,22]
# # i=0
# # s=a[0]
# # b=a[0]
# # while i<len(a):
# #     if a[i]>s:
# #         s=(a)[i]
# #     if a[i]<b:
# #         b=(a)[i]
# #     i=i+1
# # print("max",s,"min",b)
# # # # i=i+1

