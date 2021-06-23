list_numbers=[1,2,3,4,5,6,7,8,9,10]
max_num=0
second_max=list_numbers[0]
sum=0
i=0
while i<len(list_numbers):
    sum=sum+list_numbers[i]
    average=sum/len(list_numbers)
    if list_numbers[i]>max_num:
        max_num=list_numbers[i]
    if list_numbers[i]<second_max:
        second_max=list_numbers[i]
    i=i+1
print("average",average)
print(sum)
print(second_max)
print(max_num)