class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def push(self, val):
        newNode = ListNode(val)

        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

        return self
    def print(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

    def remove_duplicate(self):
        if not self.head: return self.head
        current = self.head
        while current:
            while current.next and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
            if current:
                print(current.val)
        return self.head



list = LinkList()
list.push(1)
list.push(1)
list.push(2)
list.push(3)
list.push(3)
list.push(4)

list.print()
print("========")
list.remove_duplicate()

