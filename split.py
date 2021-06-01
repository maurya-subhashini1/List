main = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
num=main.split()    
i=0
while i<len(num):
    if "over" in num:
        num.remove("over")
    i=i+1
print(num)
