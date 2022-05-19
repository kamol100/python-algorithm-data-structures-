class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        newNode = Node(val)
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
            print(current.val, end="=>")
            current = current.next





linkList = SinglyLinkList()
linkList.push(1)
linkList.push(2)
linkList.push(4)
linkList.push(6)
linkList.push(7)
linkList2 = SinglyLinkList()
linkList2.push(1)
linkList2.push(3)
linkList2.push(4)
linkList2.push(5)

linkList.print()
print("====================")
linkList2.print()
print("==================")

def merge_tow_sorted_list(list1, list2):
    l1 = list1.head
    l2 = list2.head
    newList = SinglyLinkList()
    while l1 and l2:
        if l1.val <= l2.val:
            newList.push(l1.val)
            newList.push(l2.val)
        else:
            newList.push(l2.val)
            newList.push(l1.val)
        l1 = l1.next
        l2 = l2.next
    while l1:
        newList.push(l1.val)
        l1 = l1.next
    while l2:
        newList.push(l2.val)
        l2 = l2.next
    current = newList.head
    while current:
        print(current.val,end="=>")
        current = current.next
    return newList



print(merge_tow_sorted_list(linkList, linkList2))




