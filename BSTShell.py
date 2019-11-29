Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: D:/SatyamSinha/DS Programs/BSTImplementation.py ==========
>>> bst = BSTNode(15)
>>> bst.value
15
>>> b = BST()
>>> b.insert(None, bst)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    b.insert(None, bst)
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 19, in insert
    return parent.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.insert(-1, bst)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b.insert(-1, bst)
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 15, in insert
    elif parent and node.value<=parent.value:
AttributeError: 'int' object has no attribute 'value'
>>> b.insert(BSTNode(-1), bst)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    b.insert(BSTNode(-1), bst)
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 18, in insert
    parent.right = self.insert(parent.right, node)
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 18, in insert
    parent.right = self.insert(parent.right, node)
AttributeError: 'NoneType' object has no attribute 'right'
>>> b.root
<__main__.BSTNode object at 0x05C78ED0>
>>> b.root.value
15
>>> b.insert(b.root, BSTNode(10))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b.insert(b.root, BSTNode(10))
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 16, in insert
    parent.left = self.insert(parent.left, node)
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 18, in insert
    parent.right = self.insert(parent.right, node)
AttributeError: 'NoneType' object has no attribute 'right'
>>> b.root.value
15
>>> b.root.left.value
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b.root.left.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.root.left
>>> print(b.root.left)
None
>>> b.parent
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    b.parent
AttributeError: 'BST' object has no attribute 'parent'
>>> 
========== RESTART: D:/SatyamSinha/DS Programs/BSTImplementation.py ==========
>>> bst = BSTNode(15)
>>> b = BST()
>>> 
========== RESTART: D:/SatyamSinha/DS Programs/BSTImplementation.py ==========
>>> bst = BSTNode(15)
>>> b = BST()
>>> b.insert(None, bst)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b.insert(None, bst)
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 21, in insert
    return parent.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.root
<__main__.BSTNode object at 0x05CEE530>
>>> b.root.value
15
>>> b.insert(b.root, BSTNode(10))
15
>>> b.insert(b.root, BSTNode(20))
15
>>> b.insert(b.root, BSTNode(8))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b.insert(b.root, BSTNode(8))
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 18, in insert
    parent.left = self.insert(parent.left, node)
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 17, in insert
    elif parent and node.value<=parent.value:
AttributeError: 'int' object has no attribute 'value'
>>> bst = BSTNode(8)
>>> b.insert(b.root, BSTNode(8))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    b.insert(b.root, BSTNode(8))
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 18, in insert
    parent.left = self.insert(parent.left, node)
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 17, in insert
    elif parent and node.value<=parent.value:
AttributeError: 'int' object has no attribute 'value'
>>> from BSTImplementation import BST
>>> parent
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    parent
NameError: name 'parent' is not defined
>>> insert()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    insert()
NameError: name 'insert' is not defined
>>> BST.parent
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    BST.parent
AttributeError: type object 'BST' has no attribute 'parent'
>>> b.root
<__main__.BSTNode object at 0x05CEE530>
>>> b.root.value
15
>>> 
========== RESTART: D:/SatyamSinha/DS Programs/BSTImplementation.py ==========
>>> bst = BSTNode(8)
>>> b = BST()
>>> bst = BSTNode(15)
>>> b.insert(None, bst)
'Root value:15'
>>> b.insert(b.root, BSTNode(10))
Left Node Value:10, Parent Value:15
parent:10
15
>>> b.insert(b.root, BSTNode(20))
Right Node Value:20, Parent Value:15
parent:20
15
>>> b.insert(b.root, BSTNode(8))
Left Node Value:8, Parent Value:15
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    b.insert(b.root, BSTNode(8))
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 21, in insert
    parent.left = self.insert(parent.left, node)
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 19, in insert
    elif parent and node.value<=parent.value:
AttributeError: 'int' object has no attribute 'value'
>>> 
========== RESTART: D:/SatyamSinha/DS Programs/BSTImplementation.py ==========
>>> b = BST()
>>> bst = BSTNode(15)
>>> b.insert(None, bst)
'Root value:15'
>>> b.insert(b.root, BSTNode(10))
Left Node Value:10, Parent Value:15
parent:10
<__main__.BSTNode object at 0x05ABF670>
>>> b.insert(b.root, BSTNode(8))
Left Node Value:8, Parent Value:15
Left Node Value:8, Parent Value:10
parent:8
<__main__.BSTNode object at 0x05ABF670>
>>> b.root.value
15
>>> b.root.left.value
10
>>> b.root.right.value
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    b.root.right.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.root.right
>>> b.insert(b.root, BSTNode(20))
Right Node Value:20, Parent Value:15
parent:20
<__main__.BSTNode object at 0x05ABF670>
>>> 
========== RESTART: D:/SatyamSinha/DS Programs/BSTImplementation.py ==========
>>> b = BST()
>>> b.insert(None, bst=BSTNode(8))
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    b.insert(None, bst=BSTNode(8))
TypeError: insert() got an unexpected keyword argument 'bst'
>>> b.insert(None, BSTNode(8))
'Root value:8'
>>> b.insert(b.root, BSTNode(15))
Right Node Value:15, Parent Value:8
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    b.insert(b.root, BSTNode(15))
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 21, in insert
    parent.right = self.insert(parent.right, node)
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 16, in insert
    elif node.value<=parent.value:
AttributeError: 'NoneType' object has no attribute 'value'
>>> 
========== RESTART: D:/SatyamSinha/DS Programs/BSTImplementation.py ==========
>>> b = BST()
>>> b.insert(None, BSTNode(15))
'Root value:15'
>>> b.insert(b.root, BSTNode(15))
Left Node Value:15, Parent Value:15
parent:15
<__main__.BSTNode object at 0x05D1F650>
>>> b.insert(b.root, BSTNode(20))
Right Node Value:20, Parent Value:15
parent:20
<__main__.BSTNode object at 0x05D1F650>
>>> b.insert(b.root, BSTNode(8))
Left Node Value:8, Parent Value:15
Left Node Value:8, Parent Value:15
parent:8
<__main__.BSTNode object at 0x05D1F650>
>>> b.insert(b.root, BSTNode(17))
Right Node Value:17, Parent Value:15
Left Node Value:17, Parent Value:20
parent:17
<__main__.BSTNode object at 0x05D1F650>
>>> b.insert(b.root, BSTNode(25))
Right Node Value:25, Parent Value:15
Right Node Value:25, Parent Value:20
parent:25
<__main__.BSTNode object at 0x05D1F650>
>>> b.root.value
15
>>> b.right.value
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    b.right.value
AttributeError: 'BST' object has no attribute 'right'
>>> b.root.right.value
20
>>> b.root.left.value
15
>>> b.root.right.right.value
25
>>> b.root.right.right.value
25
>>> b.root.right.right.right.value
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    b.root.right.right.right.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.root.right.left.value
17
>>> b.root.right.left.left.value
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    b.root.right.left.left.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.root.left.left.value
8
>>> b.root.left.left.left.value
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    b.root.left.left.left.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.root.left.right.value
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    b.root.left.right.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> 
========== RESTART: D:/SatyamSinha/DS Programs/BSTImplementation.py ==========
>>> b = BST(BSTNode(15))
>>> b.insert(b.root, BSTNode(10))
Left Node Value:10, Parent Value:15
parent:10
<__main__.BSTNode object at 0x05829E90>
>>> b.insert(b.root, BSTNode(20))
Right Node Value:20, Parent Value:15
parent:20
<__main__.BSTNode object at 0x05829E90>
>>> b.insert(b.root, BSTNode(8))
Left Node Value:8, Parent Value:15
Left Node Value:8, Parent Value:10
parent:8
<__main__.BSTNode object at 0x05829E90>
>>> b.insert(b.root, BSTNode(12))
Left Node Value:12, Parent Value:15
Right Node Value:12, Parent Value:10
parent:12
<__main__.BSTNode object at 0x05829E90>
>>> b.insert(b.root, BSTNode(17))
Right Node Value:17, Parent Value:15
Left Node Value:17, Parent Value:20
parent:17
<__main__.BSTNode object at 0x05829E90>
>>> b.insert(b.root, BSTNode(25))
Right Node Value:25, Parent Value:15
Right Node Value:25, Parent Value:20
parent:25
<__main__.BSTNode object at 0x05829E90>
>>> b.min_node()
(<__main__.BSTNode object at 0x05D5F450>, 8)
>>> b.insert(b.root, BSTNode(1))
Left Node Value:1, Parent Value:15
Left Node Value:1, Parent Value:10
Left Node Value:1, Parent Value:8
parent:1
<__main__.BSTNode object at 0x05829E90>
>>> b.min_node()
(<__main__.BSTNode object at 0x05D5FB10>, 1)
>>> 
========== RESTART: D:/SatyamSinha/DS Programs/BSTImplementation.py ==========
>>> b = BST()
>>> b.insert_iter(BSTNode(16))
'Root value:16'
>>> b.insert_iter(BSTNode(10))
>>> b.root.value
16
>>> b.root.right.value
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    b.root.right.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.root.left
>>> b.root.left.value
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    b.root.left.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> 
========== RESTART: D:/SatyamSinha/DS Programs/BSTImplementation.py ==========
>>> b = BST()
>>> b.insert_iter(BSTNode(16))
'Root value:16'
>>> b.insert_iter(BSTNode(10))
>>> b.root.value
16
>>> b.root.left.value
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    b.root.left.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> 
========== RESTART: D:/SatyamSinha/DS Programs/BSTImplementation.py ==========
>>> b = BST()
>>> b.insert_iter(BSTNode(16))
'Root value:16'
>>> b.insert_iter(BSTNode(10))
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    b.insert_iter(BSTNode(10))
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 66, in insert_iter
    print("Current:{}, current.right:{}".format(current.value, current.left.value))
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.insert_iter(BSTNode(20))
Right, 10
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    b.insert_iter(BSTNode(20))
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 66, in insert_iter
    print("Current:{}, current.right:{}".format(current.value, current.left.value))
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.root.value
16
>>> b.root.left.value
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    b.root.left.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.root.right.value
10
>>> 
========== RESTART: D:/SatyamSinha/DS Programs/BSTImplementation.py ==========
>>> b = BST()
>>> b.insert_iter(BSTNode(16))
'Root value:16'
>>> b.insert_iter(BSTNode(10))
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    b.insert_iter(BSTNode(10))
  File "D:/SatyamSinha/DS Programs/BSTImplementation.py", line 57, in insert_iter
    print("Left, {}".format(current.value))
AttributeError: 'NoneType' object has no attribute 'value'
>>> 
========== RESTART: D:/SatyamSinha/DS Programs/BSTImplementation.py ==========
>>> 
========== RESTART: D:/SatyamSinha/DS Programs/BSTImplementation.py ==========
>>> b = BST()
>>> b.insert_iter(BSTNode(16))
'Root value:16'
>>> b.insert_iter(BSTNode(10))
Current:16, Node:10
Previous Left 10
>>> b.insert_iter(BSTNode(20))
Current:16, Node:20
Previous Right 20
>>> b.max_node()
(<__main__.BSTNode object at 0x05899EB0>, 20)
>>> b.min_node()
(<__main__.BSTNode object at 0x05BDF470>, 10)
>>> 
