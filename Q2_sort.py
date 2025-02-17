def heapify(numbers, n, i):
    largest = i  
    left = 2 * i + 1     
    right = 2 * i + 2    
  
    
    if left < n and numbers[i] < numbers[left]:
        largest = left
  
    
    if right < n and numbers[largest] <numbers[right]:
        largest = right
  
    
    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]  
  
        
        heapify(numbers, n, largest)
  
def heapSort(numbers):
    n = len(numbers)
  
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(numbers, n, i)
  
    
    for i in range(n-1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]  
        heapify(numbers, i, 0)
  
numbers = [10,7,26,43,3,13,11]
heapSort(numbers)
print(numbers)
