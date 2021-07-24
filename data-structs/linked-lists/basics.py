from classes import LinkedList, LinkedListNode

def create_linked_list(arr:list) -> LinkedList:
    """ Description: Convert a python list into a custom Linked List
    Params: arr { list } - python list to convert
    Return: { LinkedList } - resulting linked list
    """
    ll = LinkedList()
    for i in arr:
        ll.insert(i)
    return ll

def print_linked_list(l:LinkedList):
    """ Description: Print the data held in the Linked Lists' nodes from head to tail
    Param: l { LinkedList } - Linked List to print
    Return: { None } 
    """
    result = []
    cur = l._head
    while cur is not None:
        result.append(cur._data)
        cur = cur._next
    print(" ".join([str(i) for i in result]))
    return
