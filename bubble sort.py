#Bubble sort, 25/01/2023

array = [7,9,0,6,8,4,10,190,29,389,291,292,1000]
array_len = len(array)
x = 0
rest_num = 0

print("Input Array = ",array) 

for j in array :
    for i in range(array_len-1) :
        if array[i] < array[i+1] :
            pass
        else :
            rest_num = array[i+1]
            array[i+1] = array[i]
            array[i] = rest_num
    x+=1
       
print("Sorted Array = ",array)         