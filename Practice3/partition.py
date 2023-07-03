class Node:
  def __init__(self, e, n=None):
    self.data = e
    self.next = n

def partition(head: Node, x:int) -> Node:
    curr = head
    left, mid, right = None, None, None
    while curr:
        if curr.data < x:
            if left:
                left.next = curr
                left = left.next
            else:
                head = left = curr
        else:
            if right:
                right.next = curr
                right = right.next
            else:
                mid = right = curr
        curr = curr.next
    if left:
        left.next = mid
    else:
        head = mid
    if right:
        right.next = None
    return head
