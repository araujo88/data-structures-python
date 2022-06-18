class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, node):
        node.next = self.head
        self.head = node

    def pop(self):
        if (self.head is not None):
            self.head = self.head.next

    def printStack(self):
        node = self.head
        while (node is not None):
            print(node.value)
            node = node.next

if __name__ == "__main__":
    stack1 = Stack()
    stack1.push(Node(1))
    stack1.push(Node(23))
    stack1.push(Node(42))
    stack1.printStack()
    stack1.pop()
    print("------------------")
    stack1.printStack()
    stack1.pop()
    stack1.pop()
    print("------------------")
    stack1.printStack()
