class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class SplayTree:
    def __init__(self):
        self.root = None

    def max_elem(self, key):
        while key.right != None:
            key = key.right
        return key

    def insert(self, node):
        temp = None
        root = self.root
        while root != None:
            temp = root
            if node.data < root.data:
                root = root.left
            else:
                root = root.right

        node.parent = temp
        if temp == None:
            self.root = node
        elif node.data < temp.data:
            temp.left = node
        else:
            temp.right = node

        self.__splay(node)

    def search_tree(self, node):
        current = self.root
        while current and current.data != node.data:
            if current.data < node.data:
                current = current.right
            else:
                current = current.left
        self.__splay(current)
        return current

    def __join(self, s, t):
        if s == None:
            return t

        if t == None:
            return s

        x = self.max_elem(s)
        self.__splay(x)
        x.right = t
        t.parent = x
        return x

    def delete(self, x):
        # Split
        self.__splay(x)
        if x.right != None:
            temp = x.right
            temp.parent = None
        else:
            temp = None
        s = x
        s.right = None
        # join
        if s.left != None:
            s.left.parent = None
        self.root = self.__join(s.left, temp)

    def __right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent;
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def __left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def __splay(self, x):
        while x.parent != None:
            if x.parent.parent == None:
                if x == x.parent.left:
                    # zig
                    self.__right_rotate(x.parent)
                else:
                    # zag
                    self.__left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                # zig-zig
                self.__right_rotate(x.parent.parent)
                self.__right_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                # zag-zag
                self.__left_rotate(x.parent.parent)
                self.__left_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                # zig-zag
                self.__left_rotate(x.parent)
                self.__right_rotate(x.parent)
            else:
                # zag-zig
                self.__right_rotate(x.parent)
                self.__left_rotate(x.parent)

    def preOrder(self, node):
        if (node != None):
            print(" " + str(node.data), end="")
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):
        if (node != None):
            self.inOrder(node.left)
            print(" " + str(node.data), end="")
            self.inOrder(node.right)

    def postOrder(self, node):
        if (node != None):
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(" " + str(node.data), end="")

    def printTree(self):
        print(" Preorder:")
        self.preOrder(self.root)
        print("\n Inorder:")
        self.inOrder(self.root)
        print("\n Postorder:")
        self.postOrder(self.root)


# tree = SplayTree()
# node1 = Node(9)
# node2 = Node(3)
# node3 = Node(7)
# node4 = Node(13)
# node5 = Node(32)
# node6 = Node(1)
# node7 = Node(4)
# tree.insert(node1)
# tree.insert(node2)
# tree.insert(node3)
# tree.insert(node4)
# tree.insert(node5)
# tree.insert(node6)
# tree.insert(node7)
# #tree.search_tree(node5)
# tree.delete(node5)
# tree.printTree()
# Preorder:
#  4 1 3 9 7 32 13
#  Inorder:
#  1 3 4 7 9 13 32
#  Postorder:
#  3 1 7 13 32 9 4
