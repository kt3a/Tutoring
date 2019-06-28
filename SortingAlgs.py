##selection sort 

A = [64, 25, 12, 22, 11] 
print("Unsorted list: ",A)
# Traverse through all array elements 
for i in range(len(A)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j             ##you are keeping track of the index in the list that contains the lowest valued element
            
              
    # Swap the found minimum element with  
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i]

print("Sorted with Selection Sort: ")
for i in range(len(A)):
    print(A[i])


print()

arr = [12, 11, 13, 5, 6]
print("Unsorted List: ",arr)
# Traverse through 1 to len(arr) 
for i in range(1, len(arr)): 

    key = arr[i] 

    # Move elements of arr[0..i-1], that are 
    # greater than key, to one position ahead 
    # of their current position 
    j = i-1
    while j >=0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
    arr[j+1] = key

print("Sorted with Insertion Sort: ")
for i in range(len(arr)):
    print(arr[i])
