max_list=[1,2,3,4,5,6,7,8,9,10]
min_1=max_list[0]
second_max=0
i=0
while i<len(max_list):
    if max_list[i]<min_1:
        min_1=max_list[i]
    if max_list[i]>second_max:
        second_max=max_list[i]
    i=i+1
print(second_max)
print(min_1)
