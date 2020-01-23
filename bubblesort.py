# Bubble sort program to arrange array in ascending order

# creating a bubbleSort function
def bubbleSort(arr):

    # measuring the length of array
    n = len(arr)

    # Transverse through all array elements
    for i in range(n):
    
        # Last i element is already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] == arr[j+1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print(arr)
