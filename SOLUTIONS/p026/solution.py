class Node:
    __slots__ = 'next', 'value'
    
    def __init__(self, _value, _next_element = None):
        self.value = _value
        self.next = _next_element


class SLL:
    __slots__ = 'head'
    
    def __init__(self, _head :Node):
        self.head = _head  


def _get_from_back(_list :SLL, _k :int) -> Node:
    walker = _list.head
    for _ in range(_k):
        walker = walker.next
    # check if walker is not already last so return None to signal it
    if not walker: return None
    to_find = _list.head
    while (walker.next):
        walker = walker.next
        to_find = to_find.next
    return to_find


def remove_from_back(_list :SLL, _k :int):
    predecessor = _get_from_back(_list, _k+1)
    if predecessor:
       to_remove = predecessor.next
       predecessor.next = to_remove.next
    else: # the element to remove is the head of list
       to_remove = _list.head
       _list.head = to_remove.next   
    to_remove.next = None
    element = to_remove.value
    del to_remove
    return element
