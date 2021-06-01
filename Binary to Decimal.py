b=[1, 0, 0, 1, 1, 0, 1, 1,] 
i=0
sum=0
while i<len(b):
    a=(b[-i-1])*(2**i)
    sum=sum+a
    i=i+1
print(sum)    