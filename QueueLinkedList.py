class Node:
    def __init__(self, node):
        self.value = node
        self.next = None

class Queue:
    def __init__(self, elem = None):
        self.rear = None
        self.front = None
        self.enqueue_pointer = self.front

    def enqueue(self, elem):
        elem = Node(elem)
        if self.front==None and self.rear==None:
            self.front = self.rear = elem
        else:
            self.rear.next = elem
            self.rear = elem
        return ("Front:{}, Rear:{} in Queue".format(self.front.value, self.rear.value))

    def front(self):
        return self.front.value
    def rear(self):
        return self.rear.value

    def dequeue(self):
        if self.rear==None and self.front==None:
            return (-1, "No elements in Queue")
        elif self.front == self.rear:
            self.front = self.rear = self.front.next
            return ("Front:{}, Rear:{}".format(self.front, self.rear))
        else:
            self.front = self.front.next
            return ("Queue- Front:{}, Rear:{}".format(self.front.value, self.rear.value))

class DoublyNode:
    def __init__(self, node):
        self.value = node
        self.prev = None
        self.next = None
d = DoublyNode(None)

class QueueDoubly:
    def __init__(self):
        self.rear = None
        self.front = None
        self.next = None
        self.pointer = None

    def enqueue_doubly(self, elem):
        elem = DoublyNode(elem)
        if self.front==None and self.rear==None:
            self.front = self.rear = elem
        else:
            self.pointer = self.rear
            self.rear.next = elem
            self.rear = elem
            self.rear.prev = self.pointer
        return ("Front:{}, Rear:{}".format(self.front.value, self.rear.value))

    def front(self):
        return self.front.value
    def rear(self):
        return self.rear.value

    def dequeue(self):
        if self.front==None and self.rear==None:
            return (-1, "Empty Queue")
        elif self.front == self.rear:
            self.front = self.rear = self.front.next
            return ("Front:{}, Rear:{}".format(self.front, self.rear))
        else:
            self.front = self.front.next
            return ("Queue- Front:{}, Rear:{}".format(self.front.value, self.rear.value))

    def traverse(self):
        if self.front==None and self.rear==None:
            return (-1, "Empty Queue")
        else:
            current = self.front
            while current:
                print(current.value, end = ',')
                current = current.next
