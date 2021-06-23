i=0
empty=[]
user=int(input("enter the number"))
while i<(user):
    user1=int(input("enter the number"))
    empty.append(user1)
    i=i+1
asking=int(input("enter the number"))
if asking in empty:
    print(True)
else:
    print(False)
print(empty)