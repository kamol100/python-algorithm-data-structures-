class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self

    def add_two_number(self, l1:Node, l2:Node):
        curr = Node()
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = Node(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return curr.next



    def print(self):
        curr = self.head
        if not self.head: return 0

        while curr:
            print(curr.val, end="->")
            curr = curr.next




linkList = LinkList()
linkList.push(4)
linkList.push(5)
linkList.push(6)
linkList.push(7)

print(linkList.add_two_number(Node(2), Node(5)))


