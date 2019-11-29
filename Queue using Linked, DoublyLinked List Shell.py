Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/QueueLinkedList.py ===========
>>> n = Node(3)
>>> q = Queue()
>>> q.enqueue(n)
3
>>> q.enqueue(Node(5))
3
>>> q.enqueue(Node(10))
5
>>> q.rear.value
3
>>> q.rear.next.value
5
>>> q.rear.next.next.value
10
>>> q.dequeue()
5
>>> q.rear.value
5
>>> q.rear.next.value
10
>>> q.rear.next.next.value
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    q.rear.next.next.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> a = b =2
>>> a
2
>>> b
2
>>> a is b
True
>>> a is 2
True
>>> b is 2
True
>>> a = 3
>>> b
2
>>> b = 5
>>> a
3
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/QueueLinkedList.py ===========
>>> q = Queue()
>>> q.rear.value
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    q.rear.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> q.enqueue(Node(3))
'Front:3, Rear:3 in Queue'
>>> q.enqueue(Node(5))
'Front:3, Rear:5 in Queue'
>>> q.enqueue(Node(20))
'Front:3, Rear:20 in Queue'
>>> q.dequeue()
'Queue, Front:5, Rear:20'
>>> q.dequeue()
'Queue, Front:20, Rear:20'
>>> q.dequeue()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    q.dequeue()
  File "D:/SatyamSinha/DS Programs/QueueLinkedList.py", line 41, in dequeue
    return ("Queue, Front:{}, Rear:{}".format(self.front.value, self.rear.value))
AttributeError: 'NoneType' object has no attribute 'value'
>>> q.dequeue()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    q.dequeue()
  File "D:/SatyamSinha/DS Programs/QueueLinkedList.py", line 40, in dequeue
    self.front = current.next
AttributeError: 'NoneType' object has no attribute 'next'
>>> q.rear
<__main__.Node object at 0x0598F790>
>>> q.rear.value
20
>>> q.front.value
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    q.front.value
AttributeError: 'Queue' object has no attribute 'front'
>>> q.front
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    q.front
AttributeError: 'Queue' object has no attribute 'front'
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/QueueLinkedList.py ===========
>>> q = Queue()
>>> q.dequeue()
(-1, 'No elements in Queue')
>>> q.enqueue(Node(5))
'Front:5, Rear:5 in Queue'
>>> q.dequeue()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    q.dequeue()
  File "D:/SatyamSinha/DS Programs/QueueLinkedList.py", line 40, in dequeue
    return ("Queue, Front:{}, Rear:{}".format(self.front.value, self.rear.value))
AttributeError: 'NoneType' object has no attribute 'value'
>>> q.rear.value
5
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/QueueLinkedList.py ===========
>>> q = Queue()
>>> q.enqueue(Node(5))
'Front:5, Rear:5 in Queue'
>>> q.dequeue()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    q.dequeue()
  File "D:/SatyamSinha/DS Programs/QueueLinkedList.py", line 40, in dequeue
    return ("Queue, Front:{}, Rear:{}".format(self.front.value, self.rear.value))
AttributeError: 'NoneType' object has no attribute 'value'
>>> q.rear.value
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    q.rear.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> q.front.value
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    q.front.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/QueueLinkedList.py ===========
>>> q = Queue()
>>> q.enqueue(Node(5))
'Front:5, Rear:5 in Queue'
>>> q.dequeue()
(-1, 'No elements in Queue')
>>> class DoublyNode:
	def __init__(self, node):
		self.value = node
	def print(self):
		print("Doubly", self.value)

	
>>> class Show:
	def __init__(self, val):
		self.val = val
	def show(self):
		print("Show", self.val)

		
>>> class DoublyNode:
	def __init__(self, node):
		self.value = node
	def Sh(self):
		print("Doubly", self.value)

		
>>> Show(3)
<__main__.Show object at 0x0564F470>
>>> val
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    val
NameError: name 'val' is not defined
>>> Show.val
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    Show.val
AttributeError: type object 'Show' has no attribute 'val'
>>> s = Show(3)
>>> s.val
3
>>> 
>>> class DoublyNode:
	def __init__(self, node):
		self.value = node
	def Sh(self):
		print("Doubly", self.value, Show(3))

		
>>> d = DoublyNode(5)
>>> d.value
5
>>> d.Sh()
Doubly 5 <__main__.Show object at 0x0564FCB0>
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/QueueLinkedList.py ===========
>>> q = QueueDoubly()
>>> q.enqueue_doubly(3)
'Front:3, Rear:3'
>>> q.enqueue_doubly(5)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    q.enqueue_doubly(5)
  File "D:/SatyamSinha/DS Programs/QueueLinkedList.py", line 63, in enqueue_doubly
    self.rear.next = elem
NameError: name 'elem' is not defined
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/QueueLinkedList.py ===========
>>> q = QueueDoubly()
>>> q.enqueue_doubly(3)
'Front:3, Rear:3'
>>> q.enqueue_doubly(5)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    q.enqueue_doubly(5)
  File "D:/SatyamSinha/DS Programs/QueueLinkedList.py", line 66, in enqueue_doubly
    self.rear.prev = self.pointer
AttributeError: 'int' object has no attribute 'prev'
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/QueueLinkedList.py ===========
>>> q = QueueDoubly()
>>> q.enqueue_doubly(3)
'Front:3, Rear:3'
>>> q.enqueue_doubly(5)
'Front:3, Rear:5'
>>> q.enqueue_doubly(8)
'Front:3, Rear:8'
>>> q.rear.value
8
>>> q.front.value
3
>>> q.front.next.value
5
>>> q.front.next.next.value
8
>>> q.pointer.value
5
>>> q.pointer.prev.value
5
>>> q.pointer.next.value
8
>>> q.pointer.prev.prev.value
5
>>> q.front.prev
<__main__.DoublyNode object at 0x0586F770>
>>> q.front.prev.value
3
>>> q.front.prev.prev.value
3
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/QueueLinkedList.py ===========
>>> q = QueueDoubly()
>>> q.enqueue_doubly(3)
'Front:3, Rear:3'
>>> q.enqueue_doubly(5)
'Front:3, Rear:5'
>>> q.enqueue_doubly(8)
'Front:3, Rear:8'
>>> q.front.value
3
>>> q.rear.value
8
>>> q.front.prev
>>> q.front.prev.value
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    q.front.prev.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> q.front.next.value
5
>>> q.front.next.next.value
8
>>> q.rear.prev.value
5
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/QueueLinkedList.py ===========
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/QueueLinkedList.py ===========
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/QueueLinkedList.py ===========
>>> q = Queue()
>>> q.enqueue(3)
'Front:3, Rear:3 in Queue'
>>> q.dequeue()
(-1, 'No elements in Queue')
>>> q.rear
>>> q.front
>>> q.enqueue(3)
'Front:3, Rear:3 in Queue'
>>> q.enqueue(5)
'Front:3, Rear:5 in Queue'
>>> q.dequeue()
'Queue- Front:5, Rear:5'
>>> q.enqueue(3)
'Front:5, Rear:3 in Queue'
>>> q.enqueue(8)
'Front:5, Rear:8 in Queue'
>>> q.enqueue(20)
'Front:5, Rear:20 in Queue'
>>> q.dequeue()
'Queue- Front:3, Rear:3'
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/QueueLinkedList.py ===========
>>> q = Queue()
>>> q.enqueue(3)
'Front:3, Rear:3 in Queue'
>>> q.dequeue()
'Front:None, Rear:None'
>>> q.enqueue(3)
'Front:3, Rear:3 in Queue'
>>> q.enqueue(5)
'Front:3, Rear:5 in Queue'
>>> q.dequeue()
'Queue- Front:5, Rear:5'
>>> q.enqueue(3)
'Front:5, Rear:3 in Queue'
>>> q.enqueue(8)
'Front:5, Rear:8 in Queue'
>>> q.enqueue(20)
'Front:5, Rear:20 in Queue'
>>> q.dequeue()
'Queue- Front:3, Rear:20'
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/QueueLinkedList.py ===========
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/QueueLinkedList.py ===========
>>> q = QueueDoubly()
>>> q.enqueue_doubly(3)
'Front:3, Rear:3'
>>> q.enqueue_doubly(5)
'Front:3, Rear:5'
>>> q.dequeue()
'Queue- Front:5, Rear:5'
>>> q.dequeue()
'Front:None, Rear:None'
>>> q.dequeue()
(-1, 'Empty Queue')
>>> q.enqueue_doubly(3)
'Front:3, Rear:3'
>>> q.enqueue_doubly(5)
'Front:3, Rear:5'
>>> q.enqueue_doubly(20)
'Front:3, Rear:20'
>>> q.enqueue_doubly(30)
'Front:3, Rear:30'
>>> q.traverse()
3,5,20,30,
>>> q.dequeue()
'Queue- Front:5, Rear:30'
>>> q.rear.value
30
>>> q.rear.prev.value
20
>>> 
