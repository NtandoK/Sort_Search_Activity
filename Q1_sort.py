numbers=[10,7,26,43,3,13,11]
for i in range(len(numbers)-1):
    for a in range(len(numbers)-1):
        if(numbers[a]>numbers[a+1]):
         t=numbers[a]
         numbers[a]=numbers[a+1]
         numbers[a+1]=t
         
print(numbers)         