def search(numbers,number):
    i=0
    
    while i< len(numbers):
        if numbers[i] == number:
            return False
        i=i+1
            
        return True
        
numbers=[10,7,26,43,3,13,11]
number=13        

if search(numbers,number):
    print("Found")
else:
    print ("Not Found")