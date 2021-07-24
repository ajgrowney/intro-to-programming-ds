def min_heapify(arr):
    return arr

def max_heapify(arr, i = 0, n = 0):
    left, right = 2*i, 2*i+1
    if (left <= n) and (arr[left] > arr[i]):
        largest_el = left
        arr = max_heapify(arr, largest_el, n)
    return arr

def heap_sort(arr):
	

list = [2,5,6,3,7,8]
result = max_heapify(list,0,len(list))
print(f"Max Heap: {result}")
