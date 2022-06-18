class Node:
    def __init__(self, value = None):
        self.value = value
        self.root = None
        self.left = None
        self.right = None

    def insertNodeAtLeft(self, node):
        self.left = node
        self.left.root = self.root

    def insertNodeAtRight(self, node):
        self.right = node
        self.right.root = self.root

    def printTree(self):
        print(self.value)
        node1 = self
        node2 = self
        while (node1.left is not None):
            print(node1.left.value, end = " ")
            if (node1.left.left is not None):
                print(node1.left.left.value, end = " ")
            if (node1.left.right is not None):
                print(node1.left.right.value)
            node1 = node1.left
        while (node2.right is not None):
            print(node2.right.value)
            if (node2.right.left is not None):
                print(node2.right.left.value, end = " ")
            if (node2.right.right is not None):
                print(node2.right.right.value)
            node2 = node2.right


if __name__ == "__main__":
    node1 = Node(1)
    node1.insertNodeAtLeft(Node(2))
    node1.insertNodeAtRight(Node(3))
    #node1.printTree()

    node2 = Node(23)
    node2.insertNodeAtLeft(Node(42))
    node2.insertNodeAtRight(node1)
    #node2.printTree()

    node3 = Node(69)
    node3.insertNodeAtLeft(node1)
    node3.insertNodeAtRight(node1)
    node3.printTree()


