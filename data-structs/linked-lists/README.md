# Linked List
## Description
A fundamental data structure that requires very little memory as it only tracks the number of items and a pointer to the beginning of the list

## Functions
1) insert(new_item:object, position:int) -> bool
    - Insert an item into the list at a certain position (allow to default to the end)
    - Time Complexity: O(n)

2) remove(position:int) -> bool
    - Remove an item from the list at a specific position
    - Time Complexity: O(n)
3) get_item(position:int) -> object
    - Retrieve the item stored at a specific position
    - Time Complexity: O(n)

4) replace(position:int, new_item:object) -> bool
    - Replace the item stored at a specific position with a new one
    - Time Complexity: O(n)