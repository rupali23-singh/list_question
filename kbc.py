question_list = [
    "How many continents are there?",             
    "What is the capital of India?",            
    "NG mei kaun se course padhaya jaata hai?"    
]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution_list=[3,4,1]
i=0
while i<len(question_list):
    print(i+1,question_list[i])
    j=0
    while j<len(options_list[i]):
        print(j+1,options_list[i][j])
        j=j+1
    user=int(input("enter the number/you can use 50-50"))
    if user==solution_list[i]:
        print("yes")
    else:
        print("wrong")
        break
    i=i+1

    