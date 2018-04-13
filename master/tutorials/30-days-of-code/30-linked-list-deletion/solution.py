    def removeDuplicates(self,head):
        if not head:
            return head
        current = head
        while current:
            other = current
            while other:
                while other.next and other.next.data == current.data:
                    other.next = other.next.next
                other = other.next
            current = current.next
        return head