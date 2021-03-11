binary=[1,0,0,1,1,0,1,1]
a=binary
sum=0
b=len(binary))
while a>0:
    digit=a%10
    sum=sum+digit
    a=a//10
if a%binary==0:
    print("decimal")
else:
    print("not")

