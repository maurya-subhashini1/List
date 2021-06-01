marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
] 
i=0
avg=0
while i<len(marks):
    f=0
    l=0
    sum=0
    while f<len(marks[i]):
        l=l+(marks[i][f])
        f=f+1
    sum=sum+l
    avg=sum//len(marks[i])
    print(avg)
    i=i+1




        


    
    
