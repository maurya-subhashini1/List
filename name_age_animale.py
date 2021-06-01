name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]
i=0
f=" "
while i<len(name):
    a=(name[0]+f+"the"+f+animal[0]+f+"is"+f+str(age[0]))
    b=(name[1]+f+"the"+f+animal[1]+f+"is"+f+str(age[1]))
    c=(name[2]+f+"the"+f+animal[2]+f+"is"+f+str(age[2]))
    d=(name[3]+f+"the"+f+animal[3]+f+"is"+f+str(age[3]))
    i=i+1
print(a)
print(b)
print(c)
print(d)