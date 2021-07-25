from classes import MaxHeap, MinHeap
initial_data = [11,17,9,4,3,6,2,99,8,-44]
add_data = [-66,33,21,5,18,0,-19]
heap_type = MaxHeap
heap = heap_type.heapify(initial_data)

while len(add_data) > 0:
    new_element = add_data.pop(0)
    print(f"Adding: {new_element}")
    heap.add(new_element)
    print(f'Heap: {heap._heap}')
