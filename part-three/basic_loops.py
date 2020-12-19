
loop_list = [1,2,3,4,5]

# 'for' Loop
print("For Loop")
for element in loop_list:
    print(element)


# 'while' Loop
print("While Loop")
idx = 0
end = len(loop_list)
while idx < end:
    element = loop_list[idx]
    print(element)
    
    # Increment Index
    idx = idx + 1

