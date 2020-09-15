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
  
  
    def insertAfter(self, prev_node, new_data): 
  
         
        if prev_node is None: 
            print ("The given previous node must inLinkedList.")
            return
  
        new_node = Node(new_data) 
  
        new_node.next = prev_node.next
  
        prev_node.next = new_node 
  
  
    def append(self, new_data): 
  
        new_node = Node(new_data) 
  
        if self.head is None: 
            self.head = new_node 
            return
  
        last = self.head 
        while (last.next): 
            last = last.next
  
        last.next =  new_node

    def deleteNode(self, position): 
  
            if self.head == None: 
                return 
      
            temp = self.head 
      
            if position == 0: 
                self.head = temp.next
                temp = None
                return 
      
            for i in range(position -1 ): 
                temp = temp.next
                if temp is None: 
                    break
      
            if temp is None: 
                return 
            if temp.next is None: 
                return 
      
            next = temp.next.next
      
            temp.next = None
      
            temp.next = next

    def search(self, x): 
  
            current = self.head 
      
            while current != None: 
                if current.data == x: 
                    return True 
                current = current.next
              
            return False
        
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
            self.head = prev

 

      
     
    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.data) 
            temp = temp.next
  
  
  
if __name__=='__main__': 
  
    llist = LinkedList() 
    llist.append(6) 
  
    llist.push(7); 
  
    llist.push(1); 
  
    llist.append(4) 
  
    llist.insertAfter(llist.head.next, 8) 
     
    print ('Created linked list is:'), 
    llist.printList()
    llist.deleteNode(1) 
    print ("\nLinked List after Deletion at position 4: ")
    llist.printList()
    if llist.search(6): 
        print("Yes") 
    else: 
        print("No") 
  
    llist.reverse() 
    print ("\nReversed Linked List")
    llist.printList()         
  
