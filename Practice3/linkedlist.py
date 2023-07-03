import sys
class Node:
  def __init__(self, e, n=None):
    self.data = e
    self.next = n

class LinkedList:
  def __init__(self, l=[]):
    if not l:
      self.head = None
      self.size = 0
    else:
      self.head = Node(l[0])
      self.size = len(l)
      curr = self.head
      for x in l[1:]:
        curr.next = Node(x)
        curr = curr.next

  def __len__(self):
    return self.size

  def isEmpty(self):
    return self.size == 0

  def insertToTail(self, d):
    end = Node(d)
    if not self.head:
      self.head = end
      return
    curr = self.head
    while curr.next:
      curr = curr.next
    curr.next = end

  def print(self, n=sys.maxsize):
    cnt = 0
    curr = self.head
    out = ""
    while curr and cnt < n:
      out += str(curr.data) + "->"
      curr = curr.next
      cnt += 1
    if out is not None:
      out = out[:-2]
    print(out)
