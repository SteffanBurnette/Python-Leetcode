#1- Start with the second element in the array
#2- If the second element is greater than the first element, swap them
#3- Move to the next element and compare with all previos elements (swap when needed)
#4- Repeat the process until the array is sorted

arr = [23, 1, 10, 5, 2]
#key = 0 #The key is the current element that needs to be sorted

for i in range(1, len(arr)): #Start fro the second element
    key = arr[i]
    j = i - 1 #The index of the previous element
    while j >= 0 and key < arr[j]: #Compare the current element with all previous
        arr[j + 1] = arr[j]
        j -= 1
        arr[j + 1] = key

        
print(arr)
