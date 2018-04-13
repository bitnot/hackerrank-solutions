def has_cycle(head):
    first = head.next
    last = head
    while first and first.next and last:
        if first == last or first.next == last:
            return True
        last = last.next
        first = first.next.next
    return False