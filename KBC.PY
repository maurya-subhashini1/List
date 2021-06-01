 
question_list = [
    "1 How many continents are there?",              
    "2 What is the capital of India?",            
    "3 NG mei kaun se course padhaya jaata hai?"    
]

options_list = [
    ["1 Four", "2 Nine", "3 Seven", "4 Eight"],
    ["1 Chandigarh", "2 Bhopal", "3 Chennai", "4 Delhi"],
    ["1 Software Engineering", "2 Counseling", "3 Tourism", "4 Agriculture"]
]
solution_list = [3, 4, 1]
answere_list=[
    ["1 Nine","2 seven"],
    ["1 Bhopal","2 Delhi"],
    ["1 software Engineering","2 Counseling"]
] 
ans_list = [2,2,1]
i=0
count=0
amount=10000
a=1
b=0
while i<len(question_list):
    print(question_list[i])
    j=0
    k=i
    while j<len(options_list[i]):
        print(options_list[i][j])
        j=j+1
    user=input("Do you WANT LIFE LINE")
    if user=="yes":
        print(5050)
        if count==0:
            print(answere_list[b])
            # print(answere_list[b+a])
            user2=int(input("enter the your answere:"))
            if user2==ans_list[i]:
                print("your answere correct:")
                print("you won",amount)
            else:
                print("your answere is wrong")
                print("you loose the game")
                break
            count = count+ 1
        else:
            print("sorry you csan't use lifeline again")
            user3=int(input("select your answere"))
            if user3==solution_list[i]:
                print("congrats right answere")
                print("you won",amount)
            else:
                print("your answere is wrong")
                print("you loose the game")
                break
    elif user=="no":
        user4=int(input("select your answere"))
        if user4==solution_list[i]:
            print("congrats right answere")
            print("you won",amount)
        else:
            print("your answere is wrong")
            print("you loose the game")
            break
    else:
        print("nothing")
    amount=amount+10000
    i=i+1
    a=a+1
    b=b+1


