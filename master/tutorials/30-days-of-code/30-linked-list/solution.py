    def insert(self,head,data):
        if head is None:
            return Node(data)        
        current = head
        while current.next:
            current = current.next
        current.next = Node(data)
        return head
            

  
  