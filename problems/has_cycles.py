# https://www.hackerrank.com/challenges/ctci-linked-list-cycle

def has_cycle(head):
    if head.next is None:
        return False

    visited_nodes = set()
    next = head.next
    while next is not None:
        if head.next in visited_nodes:
            return True
        visited_nodes.add(head.next)
        next = head.next
    return False
