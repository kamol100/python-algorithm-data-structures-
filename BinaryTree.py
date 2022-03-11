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



    def dfs_in_order(self, root):
        node = root
        if node is None:
            return -1
        else:
            if node.left:
                self.dfs_in_order(node.left)

            print(node.data, end=",")

            if node.right:
                self.dfs_in_order(node.right)

    def dfs_pre_order(self, root):
        node = root
        if node is None:
            return
        else:
            print(node.data, end=',')

            if node.left:
                self.dfs_pre_order(node.left)
            if node.right:
                self.dfs_pre_order(node.right)

    def dfs_post_order(self, root):
        node = root
        if node is None:
            return
        else:
            if node.left:
                self.dfs_post_order(node.left)
            if node.right:
                self.dfs_post_order(node.right)

            print(node.data, end=',')

    def levelOrder(self, root):
            if root is None:
                return
            else:
                queue = [root]
                while queue:

                    node = queue.pop(0)

                    print(node.data, end=" ")

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)






def build_tree(elements):
    root = BinaryTree()

    for i in range(0, len(elements)):
        root.insert(elements[i])

    return root

if __name__=='__main__':

    numbers = [1,2,5,3,6,4]
    tree = build_tree(numbers)

    print('In order')
    print(tree.dfs_in_order(tree.root))
    print('Pre Order')
    print(tree.dfs_pre_order(tree.root))
    print('post order')
    print(tree.dfs_post_order(tree.root))
    print('Level order')
    print(tree.levelOrder(tree.root))


