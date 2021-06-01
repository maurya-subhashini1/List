marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
counter=0
total_marks = 0
while counter<len(marks):
    num=int(marks[counter])
    total_marks=total_marks+num
    counter=counter+1
print(total_marks)
