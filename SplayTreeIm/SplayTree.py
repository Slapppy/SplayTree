import sys


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

    def insert(self, data):
        node = Node(data)
        x = self.root
        y = None

        while x != None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
        self.splay(node)


    def __binary_search(self, node, key):
        if node == None or key == node.data:
            return node
        if node.data < key:
            return self.__binary_search(node.right, key)
        return self.__binary_search(node.left, key)

    def search_tree(self, key):
        x = self.__binary_search(self.root, key)
        if x != None:
            self.splay(x)
            return key

    def delete(self):
        pass

    def right_rotate(self, x):
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

    def left_rotate(self, x):
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

    def splay(self, node):
        while node.parent != None:
            if node.parent == self.root:
                if node == node.parent.left:
                    self.right_rotate(node.parent)
                else:
                    self.left_rotate(node.parent)
            else:
                parent = node.parent
                grandParent = parent.parent
                if node.parent.left == node and parent.parent.left == parent:
                    self.right_rotate(grandParent)
                    self.right_rotate(parent)
                elif node.parent.right == node and parent.parent.right == parent:
                    self.left_rotate(grandParent)
                    self.left_rotate(parent)
                elif node.parent.right == node and parent.parent.left == parent:
                    self.left_rotate(parent)
                    self.right_rotate(grandParent)
                elif node.parent.left == node and parent.parent.right == parent:
                    self.right_rotate(parent)
                    self.left_rotate(grandParent)

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

    #  This are handling the request to display tree elements
    def printTree(self):
        print(" Preorder:")
        self.preOrder(self.root)
        print("\n Inorder:")
        self.inOrder(self.root)
        print("\n Postorder:")
        self.postOrder(self.root)


tree = SplayTree()



tree.insert(9)
tree.insert(3)
tree.insert(7)
tree.insert(13)
tree.insert(32)
tree.insert(1)
tree.insert(4)

tree.printTree()
# Preorder:
#  4 1 3 9 7 32 13
#  Inorder:
#  1 3 4 7 9 13 32
#  Postorder:
#  3 1 7 13 32 9 4
