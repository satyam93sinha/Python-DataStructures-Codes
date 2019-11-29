Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> nod = Node(3)
>>> stackLL = StackLinkedList()
>>> stackLL.push(nod)
>>> stackLL.head
<__main__.Node object at 0x061AF770>
>>> stackLL.head.node
3
>>> stackLL.push(Node(6))
>>> stackLL.push(Node(80))
>>> stackLL.peek()
<__main__.Node object at 0x061AFC50>
>>> stackLL.pop()
<__main__.Node object at 0x061AFC50>
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> stackLL = StackLinkedList()
>>> stackLL.isEmpty()
True
>>> stackLL.push(Node(6))
>>> stackLL.isEmpty()
False
>>> stackLL.peek()
6
>>> stackLL.pop()
6
>>> stackLL.isEmpty()
True
>>> stackLL.push(Node(30))
>>> stackLL.head.value
30
>>> stackLL.push(Node(300))
>>> stackLL.head.value
300
>>> stackLL.pop()
300
>>> stackLL.head.value
30
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> ll = LinkedList(Node(32))
>>> ll.append(Node(2))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    ll.append(Node(2))
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 57, in append
    current.next = elem
AttributeError: 'NoneType' object has no attribute 'next'
>>> ll.head.value
32
>>> ll.append(Node(2))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    ll.append(Node(2))
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 57, in append
    current.next = elem
AttributeError: 'NoneType' object has no attribute 'next'
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> ll = LinkedList(Node(32))
>>> ll.append(Node(2))
>>> ll.append(Node(33))
>>> ll.append(Node(800))
>>> ll.traverse
<bound method LinkedList.traverse of <__main__.LinkedList object at 0x063FF4B0>>
>>> ll.traverse()
32
2
33
800
>>> sll = StackLinkedList(Node(32))
>>> sll.head.value
32
>>> sll.reverse_linked_list(Node(32))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    sll.reverse_linked_list(Node(32))
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 35, in reverse_linked_list
    self.pop()
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 26, in pop
    self.head = temp.next
AttributeError: 'int' object has no attribute 'next'
>>> nod = Node(32)
>>> sll.reverse_linked_list(nod)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    sll.reverse_linked_list(nod)
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 33, in reverse_linked_list
    current = self.peek()
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 30, in peek
    return self.head.value
AttributeError: 'StackLinkedList' object has no attribute 'head'
>>> sll.head.value
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    sll.head.value
AttributeError: 'StackLinkedList' object has no attribute 'head'
>>> sll.head
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    sll.head
AttributeError: 'StackLinkedList' object has no attribute 'head'
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> nod = Node(3)
>>> sll = StackLinkedList(nod)
>>> sll.append(Node(32))
>>> sll.append(Node(23))
>>> sll.append(Node(200))
>>> sll.traverse()
3
32
23
200
>>> sll.reverse_linked_list(sll.head)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    sll.reverse_linked_list(sll.head)
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 50, in reverse_linked_list
    self.pop()
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 26, in pop
    self.head = temp.next
AttributeError: 'int' object has no attribute 'next'
>>> sll.push(Node(300))
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    sll.push(Node(300))
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 17, in push
    if self.head:
AttributeError: 'StackLinkedList' object has no attribute 'head'
>>> nod = Node(4)
>>> sll.push(nod)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    sll.push(nod)
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 17, in push
    if self.head:
AttributeError: 'StackLinkedList' object has no attribute 'head'
>>> sll.head.value
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    sll.head.value
AttributeError: 'StackLinkedList' object has no attribute 'head'
>>> sll = StackLinkedList()
>>> sll.push(Node(5))
>>> sll.head.value
5
>>> sll.push(Node(2))
>>> sll.traverse()
2
5
>>> sll.reverse_linked_list()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    sll.reverse_linked_list()
TypeError: reverse_linked_list() missing 1 required positional argument: 'head'
>>> sll.reverse_linked_list(sll.head)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    sll.reverse_linked_list(sll.head)
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 50, in reverse_linked_list
    self.pop()
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 26, in pop
    self.head = temp.next
AttributeError: 'int' object has no attribute 'next'
>>> def fun():
	s = 3

	
>>> fun().s
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    fun().s
AttributeError: 'NoneType' object has no attribute 's'
>>> fun()
>>> fun.s
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    fun.s
AttributeError: 'function' object has no attribute 's'
>>> fun()
>>> s
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> sll = StackLinkedList(Node(3))
>>> sll.push(2)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    sll.push(2)
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 19, in push
    node.next = self.head
AttributeError: 'int' object has no attribute 'next'
>>> sll.push(Node(2))
>>> sll.push(Node(20))
>>> sll.traverse()
20
2
3
>>> sll.reverse_linked_list()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    sll.reverse_linked_list()
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 47, in reverse_linked_list
    current.next = self.list_.pop()
IndexError: pop from empty list
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> sll = StackLinkedList(Node(3))
>>> sll.push(Node(2))
>>> sll.push(Node(20))
>>> sll.traverse()
20
2
3
>>> sll.reverse_linked_list()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    sll.reverse_linked_list()
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 46, in reverse_linked_list
    current.next = self.list_.pop()
IndexError: pop from empty list
>>> sll.list_
[]
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> sll = StackLinkedList(Node(3))
>>> sll.push(Node(2))
>>> sll.reverse_linked_list()
[<__main__.Node object at 0x061AF870>]
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    sll.reverse_linked_list()
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 47, in reverse_linked_list
    current.next = self.list_.pop()
IndexError: pop from empty list
>>> sll.list_
[]
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> sll = StackLinkedList(Node(3))
>>> sll.push(Node(2))
>>> sll.reverse_linked_list()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    sll.reverse_linked_list()
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 41, in reverse_linked_list
    self.list_.append(current)
AttributeError: 'StackLinkedList' object has no attribute 'list_'
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> sll = StackLinkedList(Node(3))
>>> sll.push(Node(2))
>>> sll.reverse_linked_list()
[<__main__.Node object at 0x05ADF8F0>]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    sll.reverse_linked_list()
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 47, in reverse_linked_list
    current.next = self.list_.pop()
IndexError: pop from empty list
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> sll = StackLinkedList(Node(3))
>>> sll.push(Node(2))
>>> sll.reverse_linked_list()
[<__main__.Node object at 0x062AF930>]
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    sll.reverse_linked_list()
  File "D:/SatyamSinha/DS Programs/StackLinkedList.py", line 47, in reverse_linked_list
    current.next = list_.pop()
IndexError: pop from empty list
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> sll = StackLinkedList(Node(3))
>>> sll.push(Node(2))
>>> sll.reverse_linked_list()
[<__main__.Node object at 0x05BAF910>]
>>> sll.traverse()
3
2
>>> sll.reverse_linked_list()
[<__main__.Node object at 0x05BAF7B0>]
>>> sll.traverse()
2
3
>>> i = )
SyntaxError: invalid syntax
>>> i = 1 or 2 or 3
>>> i
1
>>> i = (1 or 2 or 3)
>>> i
1
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> sll = StackLinkedList()
>>> sll.balanced_parenthesis("[{}()]")
[]
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> sll = StackLinkedList()
>>> sll.balanced_parenthesis("[{}()]")
'Unbalanced'
>>> sll.stack
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    sll.stack
AttributeError: 'StackLinkedList' object has no attribute 'stack'
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> sll = StackLinkedList()
>>> sll.balanced_parenthesis("[{}()]")
('Unbalanced', ['[', '{', '}', '(', ')'])
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> 
=========== RESTART: D:/SatyamSinha/DS Programs/StackLinkedList.py ===========
>>> sll = StackLinkedList()
>>> sll.balanced_parenthesis("[{}()]")
[] 3
>>> l = [1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1]
>>> l.count(1)
15
>>> 
