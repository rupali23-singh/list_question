numbers=[50,40,23,70,56,12,5,10,7]
max=0
i=0
secondmax=0
while i<len(numbers):
    if numbers[i]>max:
        secondmax=max
        max=numbers[i]
        if secondmax<numbers[i] and max>numbers[i]:
            max=numbers
    i=i+1  
print(secondmax)