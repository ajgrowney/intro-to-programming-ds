class MinHeap:
    def __init__(self) -> None:
        self._count = 0
        self._heap = []

    @staticmethod
    def make_heap(arr, pos) -> list:
        """ Description: static method to 
        """
        resolved = False
        while not resolved:

            # Determine which element to be swapped with
            left_pos, right_pos = int(pos*2 + 1), int(pos*2 + 2)
            if right_pos < len(arr):
                swap_pos = right_pos if (arr[right_pos] < arr[left_pos]) else left_pos
                if arr[pos] < arr[swap_pos]:
                    swap_pos = None
            elif left_pos < len(arr):
                if arr[pos] > arr[left_pos]:
                    swap_pos = left_pos
                else:
                    swap_pos = None
            else:
                swap_pos = None
            
            if swap_pos is None:
                resolved = True
            else:
                tmp = arr[swap_pos]
                arr[swap_pos] = arr[pos]
                arr[pos] = tmp
                pos = swap_pos
        return arr
    

    @classmethod
    def heapify(cls, arr) -> 'MinHeap':
        """ Description: static method to min heapify a list 
        """
        new_heap = cls()
        new_heap._count = len(arr)
        cur = int(len(arr) / 2)
        while cur >= 0:
            arr = cls.make_heap(arr,cur)
            cur += -1
        new_heap._heap = arr
        return new_heap
    
    def peek_top(self) -> int:
        if self._count == 0:
            raise Exception("Heap is empty")
        else:
            return self._heap[0]

    def add(self, new_item:int) -> bool:
        cur_pos  = self._count
        self._heap.append(new_item)
        if self._count != 0:
            resolved = False
            while not resolved:
                parent_pos = int((cur_pos - 1) / 2)
                cur_parent = self._heap[parent_pos]
                if new_item < cur_parent:
                    self._heap[cur_pos] = cur_parent
                    self._heap[parent_pos] = new_item
                    cur_pos = parent_pos
                    resolved = False
                else:
                    resolved = True
        self._count += 1
        return True
    
    def remove(self) -> bool:
        return False

class MaxHeap:
    def __init__(self) -> None:
        self._count = 0
        self._heap = []
    
    @staticmethod
    def make_heap(arr, pos) -> list:
        """ Description: static method to 
        """
        resolved = False
        while not resolved:

            # Determine which element to be swapped with
            left_pos, right_pos = int(pos*2 + 1), int(pos*2 + 2)
            if right_pos < len(arr):
                swap_pos = right_pos if (arr[right_pos] > arr[left_pos]) else left_pos
                if arr[pos] > arr[swap_pos]:
                    swap_pos = None
            elif left_pos < len(arr):
                if arr[pos] < arr[left_pos]:
                    swap_pos = left_pos
                else:
                    swap_pos = None
            else:
                swap_pos = None
            
            if swap_pos is None:
                resolved = True
            else:
                tmp = arr[swap_pos]
                arr[swap_pos] = arr[pos]
                arr[pos] = tmp
                pos = swap_pos
        return arr

    @classmethod
    def heapify(cls, arr) -> 'MaxHeap':
        """ Description: static method to min heapify a list 
        """
        new_heap = cls()
        new_heap._count = len(arr)
        cur = int(len(arr) / 2)
        while cur >= 0:
            arr = cls.make_heap(arr,cur)
            cur += -1
        new_heap._heap = arr
        return new_heap
    
    def peek_top(self) -> int:
        if self._count == 0:
            raise Exception("Heap is empty")
        else:
            return self._heap[0]
    
    def add(self, new_item:int) -> bool:
        cur_pos = self._count
        self._heap.append(new_item)
        if self._count != 0:
            resolved = False
            while not resolved:
                parent_pos = int((cur_pos - 1) / 2)
                cur_parent = self._heap[parent_pos]
                if new_item > cur_parent:
                    self._heap[cur_pos] = cur_parent
                    self._heap[parent_pos] = new_item
                    cur_pos = parent_pos
                    resolved = False
                else:
                    resolved = True
        self._count += 1
        return True
    
    def remove(self) -> bool:
        if self._count <= 0:
            raise Exception("Heap is empty")
        elif self._count == 1:
            del self._heap[0]
            self._count = 0
            self._heap = []
        else:
            self._heap[0] = self._heap[self._count-1]
            del self._heap[self._count-1]
            self._count += -1
            cur_pos, resolved = 0, False
            while not resolved:
                cur_value = self._heap[cur_pos]
                cur_left, cur_right = ((2*cur_pos)+1), ((2*cur_pos)+2)
                if cur_right < self._count:
                    swap = cur_right if (self._heap[cur_right] > self._heap[cur_left]) else cur_left
                    if self._heap[cur_pos] > self._heap[swap]:
                        swap = None
                elif (cur_left < self._count) and (self._heap[cur_pos] < self._heap[cur_left]):
                    swap = cur_left
                else:
                    swap = None
                
                if swap is not None:
                    self._heap[cur_pos] = self._heap[swap]
                    self._heap[swap] = cur_value
                    cur_pos = swap
                else:
                    resolved = True
        return True