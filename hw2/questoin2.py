# Given an array, rotate the array to the right by k steps, where k is non-negative.


# Questions
# -----------
# Are all data types the same
# sorted or unordered

# Assumptions
# -----------
# That one data type is moving at a time

# How I would solve this
# -----------
# creating a loop to look through the range of the array and move the first index to the final postion and at the same time to 
# move the other indicies one spot forward

# Solution
# -----------


rotate_num = 3
list_1 = [2, 'no', 4.2, 3, 1, 'yes']

def rightRotate(lists, number): 
    
    number_rotate_list = [] 
      
    for element in range(len(lists) - number, len(lists)): 
        number_rotate_list.append(lists[element]) 
      
    for element in range(0, len(lists) - number):  
        number_rotate_list.append(lists[element]) 
          
    return number_rotate_list 

print(rightRotate(list_1, rotate_num)) 