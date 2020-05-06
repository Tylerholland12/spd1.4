def duplicate_numbers(lst, size): 
      
    for index in range(0, size): 
          
        if lst[abs(lst[index])] >= 0: 
            lst[abs(lst[index])] = -lst[abs(lst[index])] 
        else: 
            print(abs(lst[index]))


lst = [2, 4, 2, 5, 6, 7, 9, 3, 5, 1, 4] 
array_size = len(lst) 
  
duplicate_numbers(lst, array_size) 

"""
The time complexity of this function is O(n) because it is looping through the
array and taking out any numbers that are duplicates
"""