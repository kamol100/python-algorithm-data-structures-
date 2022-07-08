class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            current = newNode
            while current:
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = newNode
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = newNode
                        break

def build_tree(elements):
    root = BinaryTree()

    for i in range(0, len(elements)):
        root.insert(elements[i])

    return root

if __name__=='__main__':

    numbers = [4,2,3,1,7,6]
    tree = build_tree(numbers)

def is_same_tree(p:Node, q:Node):
    if not p and not q:
        return True
    if not p or not q or p.data != q.data:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

