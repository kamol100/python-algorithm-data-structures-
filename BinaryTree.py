class BinaryTree:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BinaryTree(data)


    def dfs_in_order(self):

        if self.left:
            self.left.dfs_in_order()

        print(self.data, end=",")

        if self.right:
            self.right.dfs_in_order()

    def dfs_pre_order(self):

        print(self.data, end=',')
        if self.left:
            self.left.dfs_pre_order()
        if self.right:
            self.right.dfs_pre_order()




def build_tree(elements):
    root = BinaryTree(elements[0])

    for i in range(1, len(elements)):
        root.insert(elements[i])

    return root

if __name__=='__main__':

    numbers = [17,4,1,20,9,23,18,34]
    tree = build_tree(numbers)
    print('In order')
    print(tree.dfs_in_order())
    print('Pre Order')
    print(tree.dfs_pre_order())


