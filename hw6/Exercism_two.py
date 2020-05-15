rotate_num = 3
# list_1 = [2, 'no', 4.2, 3, 1, 'yes']
list_1 = [6, "+", -8]

def rightRotate(lists, number): 
    
    number_rotate_list = [] 
      
    for element in range(len(lists) - number, len(lists)): 
        number_rotate_list.append(lists[element]) 
      
    for element in range(0, len(lists) - number):  
        number_rotate_list.append(lists[element]) 
          
    return number_rotate_list 

print(rightRotate(list_1, rotate_num)) 