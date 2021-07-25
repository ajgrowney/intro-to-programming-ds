from helpers import create_linked_list, print_linked_list
data = [1,2,3,4,5,6,7]
l = create_linked_list(data)
print_linked_list(l)

while l._count > 0:
    l.remove(0)