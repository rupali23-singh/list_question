list_1=[1,2,3,4,5,6,66,7]
even_nums=0
odd_nums=0
for x in (list_1):
    if(x%2==0):
        even_nums+=1
    else:
        odd_nums+=1
print("even numbers are:",even_nums)
print("odd numbers are:",odd_nums)