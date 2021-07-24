class LinkedListNode:
    def __init__(self, data) -> None:
        self._data = data
        self._next = None

class LinkedList:
    def __init__(self) -> None:
        self._head = None
        self._count = 0
    
    def insert(self, new_item:object, position:int = None) -> bool:
        try:
            # Handle position resolution / exception
            if position is None:
                position = self._count
            elif position > self._count:
                raise Exception("Position exceeded Linked List size")
            
            # Iterate to the place we need to insert
            cur_position, cur_node = 0, self._head
            while cur_position < (position-1):
                # print(cur_position, position)
                cur_node = cur_node._next
                cur_position += 1
            
            # Create the new node
            new_node = LinkedListNode(new_item)
            
            # Insert the new node at the position
            if cur_node is not None:
                tmp = cur_node._next
                cur_node._next = new_node
                new_node._next = tmp

            # If the new node was inserted at the start, set the LL head
            if position == 0:
                self._head = new_node
            
            self._count += 1
            return True
        except Exception as e:
            print(f"Exception: {e}")
            return False

    def remove(self, position:int) -> bool:
        """ Description: Remove an item from the list at a specific position
        Param: position { int } - Position in the 0-indexed Linked List to remove
        Return: { bool } - If the operation was successful        
        """
        try:
            # Error Handling
            if position >= self._count:
                raise Exception("Position exceeded the (0-indexed) Linked List size")
            
            # Iterate to position
            cur_position, cur_node, prev_node = 0, self._head, None
            while cur_position < position:
                prev_node = cur_node
                cur_node = cur_node._next
                cur_position += 1
            
            if prev_node is not None:
                prev_node._next = cur_node._next
            elif position == 0:
                self._head = cur_node._next
            
            del cur_node
            self._count += -1
            return True
        except Exception as e:
            return False
    
    def get_item(self, position:int) -> object:
        """ Description: Retrieve the item stored at a specific position
        Param: position { int } - Position in the 0-indexed Linked List to remove
        Return: { object } - Data stored at the position requested
        """
        try:
            # Error Handling
            if position >= self._count:
                raise Exception("Position exceeded the (0-indexed) Linked List size")
            # Iterate to position
            cur_position, cur_node = 0, self._head
            while cur_position < position:
                cur_position += 1
                cur_node = cur_node._next
            
            # Get and Return Data
            return cur_node._data
        except Exception as e:
            return False

    def replace(self, position:int, new_item:object) -> bool:
        """ Description: Replace the item stored at a specific position with a new one
        Param: position { int } - Position in the 0-indexed Linked List to remove
        Param: new_item { object } - Data to replace existing item with
        Return: { bool } - If the operation was successful
        """
        try:
            # Error Handling
            if position >= self._count:
                raise Exception("Position exceeded the (0-indexed) Linked List size")
            # Iterate to position
            cur_position, cur_node = 0, self._head
            while cur_position < position:
                cur_position += 1
                cur_node = cur_node._next
            cur_node._data = new_item
            return True
        except Exception as e:
            return False