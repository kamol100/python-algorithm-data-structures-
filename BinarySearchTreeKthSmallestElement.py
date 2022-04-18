class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while current:
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(data)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(data)
                        break

    def k_th_smallest_element(self, root, k):
        stack = []
        current = root
        i = 0
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            i += 1
            if i == k:
                return current.data
            current = current.right







def build_tree(elements):
    root = BinaryTree()

    for i in range(0, len(elements)):
        root.insert(elements[i])

    return root
if __name__=='__main__':

    numbers = [20,8,22,4,12,10,14]
    tree = build_tree(numbers)

    print(tree.k_th_smallest_element(tree.root,5))
