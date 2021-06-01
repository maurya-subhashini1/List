 
maigic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
] 
i=0
sum=0
while i<len(maigic_square):
    col=0
    while col<len(maigic_square):
        sum=sum+maigic_square[i][col]
        col=col+1
    j=0
    s=0
    while j<len(maigic_square):
        col=0
        while col<len(maigic_square):
            s=s+maigic_square[i][col] 
            col=col+1
        j=j+1
        k=0
        a=0
        while k<len(maigic_square):
            dig=0
            while dig<len(maigic_square):
                a=a+maigic_square[i][dig]
                dig=dig+1
            k=k+1
    i=i+1
print(sum)
print(s)
print(a)
if sum==s==a:
    print("its maigic_square")
else:
    print("its not maigic_square")
  
