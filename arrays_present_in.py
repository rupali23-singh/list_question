# list=[1,2,3,4,5,6,7]
# list_1=[2,3,1,0,6,7]
# i=0
# empty=[]
# while i<len(list_1):
#     if list[i] not in list_1:
#         empty.append(list[i])
#     i=i+1
# print(empty)
num=int(input("enter the number"))
sum1=list=[1,2,3,4,5,6,7]
# list_1=[2,3,1,0,6,7]
# i=0
# empty=[]
# while i<len(list_1):
#     if list[i] not in list_1:
#         empty.append(list[i])
#     i=i+1
# print(empty)
while (num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
        sum1=sum1+f
        num=num//10
if (sum1==tem):
    print("strong number")
else:
    print("none")