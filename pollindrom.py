# Palindrome wo strings ya numbers hote hai jo ulta seedhe same hote hai.
#  Jaise, NITIN. Nitin ko aap left se padho ya right se, nitin hi hai. 
#  Aise hi MOM bhi ek palindrome hai. 
#  Code likho jo check kare ki kya list palindrome hai ya nahi. 
#  Aur print karo “Haan! palindrome hai” agar hai.
#   Aur “nahi! Palindrome nahi hai” agar nahi hai. 
#   Abhi ke liye iss list ko use kar ke code likh sakte ho:

num=["n","i","t","n"]
i=0
a=[]
while i<len(num):
    n=num[i]
    n=num[len(num)-i-1]
    a.append(n)
    i=i+1
if a==num:
    print("it is palindrom") 
else:
    print("it is not palindrom") 