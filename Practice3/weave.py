import sys

class Node:
    def __init__(self, d, n=None):
        self.data = d
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

    def weave(self):
        fast = self.head
        slow = self.head
        while fast.next.next:
            fast = fast.next.next
            slow = slow.next
        p1 = self.head
        p2 = slow.next
        while p1.next != slow.next:
            temp_p1 = p1.next
            p1.next = p2
            temp_p2 = p2.next
            p2.next = temp_p1
            p1 = temp_p1
            p2 = temp_p2
        p1.next = p2            

if __name__ == '__main__':
    if len(sys.argv):
        l = sys.argv[1:]
        L = LinkedList(l)
        L.weave()
        L.print()

        
