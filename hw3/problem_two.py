class Node:  
  
    def __init__(self, data):  
        self.data = data  
        self.next = None 
  
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    def printmiddlevalue(self): 
        slow_pointer = self.head 
        fast_pointer = self.head 
  
        if self.head != None: 
            while (fast_pointer != None and fast_pointer.next != None): 
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next
            print("The value of the middle index is", slow_pointer.data) 
  

list1 = LinkedList() 
 
list1.push(0) 
list1.push(-9) 
list1.push(13) 

list1.printmiddlevalue() 