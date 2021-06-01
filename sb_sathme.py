a =[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
h=[]
j=[]
sum=0
s=0
avg=0
av=0
count=0
c=0
totale=0
avrege=0
while i<len(a):
    b=a[i]
    if b%2==0:
        sum=sum+b
        h.append(b)
        avg=sum//len(h)
        count=count+1   
    else:
        s=s+b
        j.append(b)
        av=sum//len(j)
        c=c+1
        totale=sum+s
        avrege=avg+av
    i=i+1
print("even number=",h,sum,"avrege=",avg,"odd number=",j,s,"avrege=",av,)
print("even count=",count,"odd count=",c)
print("totale sum=",totale)
print("totale avrege=",avrege)
