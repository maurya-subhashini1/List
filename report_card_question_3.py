marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
] 
i=0
sum=0
while i<len(marks):
    j=0
    h=0
    while j<len(marks[i]):
        h=h+(marks[i][j])
        j=j+1
    sum=sum+h
    i=i+1
print(sum)