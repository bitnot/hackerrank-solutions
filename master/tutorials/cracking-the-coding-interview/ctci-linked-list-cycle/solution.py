"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
def has_cycle(head):
    first = head.next
    last = head
    while first and first.next and last:
        if first == last or first.next == last:
            return True
        last = last.next
        first = first.next.next
    return False