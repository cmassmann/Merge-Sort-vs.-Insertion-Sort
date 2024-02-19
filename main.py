import timeit
import random

# https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertionSort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key

# https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # Into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# https://www.geeksforgeeks.org/timeit-python-examples/
def insertion_time():
    SETUP_CODE = '''
from __main__ import insertionSort
import random'''
 
    TEST_CODE = '''
mylist = [x for x in range(85)]
random.shuffle(mylist)
insertionSort(mylist)'''
 
    # timeit.repeat statement
    times = timeit.repeat(stmt=TEST_CODE,
                          setup=SETUP_CODE,
                          repeat=1,
                          number=85)
 
    # printing minimum exec. time
    print('Insertion Sort time: {}'.format(min(times)))
 
# compute merge sort time
def merge_time():
    SETUP_CODE = '''
from __main__ import mergeSort
import random'''
 
    TEST_CODE = '''
mylist = [x for x in range(85)]
random.shuffle(mylist)
mergeSort(mylist)
    '''
    # timeit.repeat statement
    times = timeit.repeat(stmt=TEST_CODE,
                          setup=SETUP_CODE,
                          repeat=1,
                          number=85)
 
    # printing minimum exec. time
    print('Merge Sort time: {}'.format(min(times)))
 
 
if __name__ == "__main__":
    insertion_time()
    merge_time()