start_list=[2,3,15,15,3,2]
i=0
last_list=start_list[i]
while i<len(start_list):
    if start_list[i] !=last_list:
        print(i,"equal")
    else:
        print(i,"not equal")
    i=i+1
      