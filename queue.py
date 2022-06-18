class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, node):
        if (self.head is None):
            self.head = node
        else:
            innerNode = self.head
            while(innerNode.next is not None):
                innerNode = innerNode.next
            innerNode.next = node
        
    def dequeue(self):
        self.head = self.head.next

    def printQueue(self):
        node = self.head
        while(node is not None):
            print(node.value)
            node = node.next
       

if __name__ == "__main__":
    queue1 = Queue()
    queue1.enqueue(Node(1))
    queue1.enqueue(Node(2))
    queue1.enqueue(Node(3))
    queue1.printQueue()
    print("------------------")
    queue1.dequeue()
    queue1.printQueue()
    print("------------------")
