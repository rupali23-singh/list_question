# a=[1,2,4,6,8,9,10]
# max_1=0
# smax=0
# i=0
# while i<len(a):
#     if a[i]>max_1:
#         smax=max_1
#         max_1=a[i]
#         if smax<a[i] and max_1>a[i]:
#             max_1=a[i]
#     i=i+1
# print(smax)
user=[50,100,67,34,23,70,5,10]
max=0
second_max=0
third_max=0
empty=0
i=0
while i<len(user):
    j=0
    c=0
    while j<len(user):
        if user[i]>max:
            c+=1
        second_max=max=third_max
        max=user[i]
        if second_max<user[i]and max>user[i]and third_max<user[i]:
            j+=1
    i=i+1
print(max,second_max,third_max)
