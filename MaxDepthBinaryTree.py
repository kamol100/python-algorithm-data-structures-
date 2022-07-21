class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while current:
                if val and val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break


    def print_tree(self, root):
        current = root
        if current.left:
            self.print_tree(root.left)
        print(current.val, end=",")
        if current.right:
            self.print_tree(root.right)





    def max_depth_of_binary_tree(self, root):
        if not root:
            return 0
        return 1 + max(self.max_depth_of_binary_tree(root.left), self.max_depth_of_binary_tree(root.right))



def build_tree(elements):
    root = BinaryTree()
    for i in range(0, len(elements)):
        root.insert(elements[i])

    return root
if __name__=='__main__':

    numbers = [27,14,35,10,19,31,42]
    #numbers = [3,9,20,None, None, 15,7]
    tree = build_tree(numbers)
    #tree.print_tree(tree.root)
    print(tree.max_depth_of_binary_tree(tree.root))


