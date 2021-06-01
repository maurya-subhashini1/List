# Yeh kisi student ke peechle teen saal ke marks hai.
#  Aap ko teeno saalo, ke sab subjects ke marks ka total calculate karna hai. 
#  Jaise uppar di hui nested list ka sum - 1142 aayega.
#   # Edge Cases: Check your program for following nested lists as well (bina code change kiye chalna chahiye,
#  nahi toh aapne sahi se code nahi likha):

marks=[
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
] 
i=0
sum=0
count=0
while i<len(marks):
    num=marks[i]
    a=num[0]+num[1]+num[2]+num[3]+num[4]
    a=num[0]+num[1]+num[2]+num[3]+num[4]
    a=num[0]+num[1]+num[2]+num[3]+num[4]
    sum=sum+a
    count=count+1
    i=i+1
print("Total Marks=",sum,"count",count) 
