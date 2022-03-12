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
            return
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


    def topView(self, root):

        queue = [(root,0)]
        result = {}
        while queue:
            node = queue.pop(0)

            if node[1] not in result:
                result[node[1]] = node[0].data

            if node[0].left:
                queue.append((node[0].left,node[1]-1))
            if node[0].right:
                queue.append((node[0].right, node[1]+1))

        for item in sorted(result):
            print(result[item], end=" ")









def build_tree(elements):
    root = BinaryTree()

    for i in range(0, len(elements)):
        root.insert(elements[i])

    return root

if __name__=='__main__':

    numbers = [1,2,5,3,6,4]
    numbers2 = [
        37, 23, 108, 59, 86, 64, 94, 14, 105, 17, 111, 65, 55, 31, 79, 97, 78, 25, 50, 22, 66,
        46, 104, 98, 81, 90, 68, 40, 103, 77, 74, 18, 69, 82, 41, 4,
        48, 83, 67, 6, 2, 95, 54, 100, 99, 84, 34, 88, 27, 72, 32, 62, 9, 56, 109, 115, 33, 15, 91,
        29, 85, 114, 112, 20, 26, 30, 93, 96, 87, 42, 38, 60, 7,
        73, 35, 12, 10, 57, 80, 13, 52, 44, 16, 70, 8, 39, 107, 106, 63, 24, 92, 45,
        75, 116, 5, 61, 49, 101, 71, 11, 53, 43, 102, 110, 1, 58, 36, 28, 76,
        47, 113, 21, 89, 51, 19, 3
    ]
    tree = build_tree(numbers2)

    print('In order')
    print(tree.dfs_in_order(tree.root))
    print('Pre Order')
    print(tree.dfs_pre_order(tree.root))
    print('post order')
    print(tree.dfs_post_order(tree.root))
    print('Level order')
    print(tree.levelOrder(tree.root))
    print('Top view')
    print(tree.topView(tree.root))


