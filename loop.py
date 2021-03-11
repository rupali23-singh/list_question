num=int(input("enter the number="))
a=num
sum=0
b=len(str(num))
while a>0:
    digit=a%10
    sum=sum+digit
    a=a//10
if a%num==0:
    print("it is harshad number=")
else:
    print("this is not harshad number=")
    