class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def findNode(self, node):
        innerNode = self.head
        while innerNode is not None:
            if (innerNode.value == node.value):
                return True
            innerNode = innerNode.next
        return False

    def insertAtHead(self, node):
        node.next = self.head
        self.head = node

    def insertAtBottom(self, node):
        if (self.head is None):
            self.head = node
        else:
            innerNode = self.head
            while innerNode.next is not None:
                innerNode = innerNode.next
            innerNode.next = node


if __name__ == "__main__":
    linkedlist1 = LinkedList()
    linkedlist1.insertAtHead(Node(1))
    linkedlist1.insertAtHead(Node(2))
    linkedlist1.insertAtHead(Node(3))
    linkedlist1.insertAtBottom(Node(69))
    linkedlist1.printList()
    print(linkedlist1.findNode(Node(1)))
    print(linkedlist1.findNode(Node(42)))