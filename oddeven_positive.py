# user=int(input("enter the number"))
# i=0
# while i<user:
#     user1=int(input("enter the number"))
#     if usre1!=0:
#         print("zero")
#     if user1>=0:
#         print("positvie number")
#         i=i+1
#     else:
#         print("negative number")
#     if user1%2==0:
#         print("even")
#     else:
#         print("odd")
user=int(input("enter the number"))
i=0
while i<user:
    user1=int(input("enter the number"))
    if user1==0:
        if user1>=0:
            print("zero")
        else:
            print("positive number")
        i=i+1
    else:
        print("negative number")
    if user1%2==0:
        print("even")
    else:
        print("odd")