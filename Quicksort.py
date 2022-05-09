import random
import time
import numpy as np

# Generated List of number(low, high, size)
array = np.random.randint(0, 600000, 5000).tolist()
# print(array)

# Quicksort function
def quick_sort(arr):

    # Recursion Algorithm
    if len(arr) < 2:
        # Base case including 0 or 1 element to stop recursion algorithm for unlimited loop recursion
        return arr

    else:
        # pivot point that divide array to solve the problem between less_nm + pivot + greater_nm
        # random number is a good choice more than first position for prevention worst-case scenario
        random.shuffle(arr)
        pivot = [arr[0]]
        # List of number that more valueable than pivot number
        greater_nm = [i for i in arr[1:] if i > pivot[0]]
        # List of number that less valueable than pivot number
        less_nm = [i for i in arr[1:] if i <= pivot[0]]
        # combined all number 
        return quick_sort(less_nm) + pivot + quick_sort(greater_nm)

# Algorithm that spend in time
start = time.time()
quick_sort(array)
print(f"The Quicksort algorithm use {(time.time() - start)*1000000} μs")