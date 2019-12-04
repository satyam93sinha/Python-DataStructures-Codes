Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: D:\SatyamSinha\DS Programs\BSTImplementation.py ==========
>>> 
========== RESTART: D:\SatyamSinha\DS Programs\BSTImplementation.py ==========
>>> b = BST()
>>> b.insert(None, 20)
'Root value:20'
>>> b.insert(b.root, 15)
Left Node Value:15, Parent Value:20
parent:<__main__.BSTNode object at 0x0624F510>
<__main__.BSTNode object at 0x0624F7B0>
>>> b.insert(b.root,30)
Right Node Value:30, Parent Value:20
parent:<__main__.BSTNode object at 0x0624FB30>
<__main__.BSTNode object at 0x0624F7B0>
>>> b.insert(b.root, 10)
Left Node Value:10, Parent Value:20
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b.insert(b.root, 10)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 23, in insert
    parent.left = self.insert(parent.left, node)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 21, in insert
    elif node.value<=parent.value:
TypeError: '<=' not supported between instances of 'BSTNode' and 'BSTNode'
>>> b.root.value
20
>>> b.root.left.value
<__main__.BSTNode object at 0x0624F510>
>>> b.root.left.value
<__main__.BSTNode object at 0x0624F510>
>>> b.root.right.value
<__main__.BSTNode object at 0x0624FB30>
>>> b.root.right
<__main__.BSTNode object at 0x0624F5F0>
>>> 
========== RESTART: D:\SatyamSinha\DS Programs\BSTImplementation.py ==========
>>> b = BST()
>>> b.insert(None, BSTNode(20))
'Root value:20'
>>> b.insert(b.root, BSTNode(15))
Left Node Value:15, Parent Value:20
parent:15
<__main__.BSTNode object at 0x05D6F770>
>>> b.root.left.value
15
>>> b.insert(b.root, BSTNode(30))
Right Node Value:30, Parent Value:20
parent:30
<__main__.BSTNode object at 0x05D6F770>
>>> b.root.right.value
30
>>> b.insert(b.root, BSTNode(10))
Left Node Value:10, Parent Value:20
Left Node Value:10, Parent Value:15
parent:10
<__main__.BSTNode object at 0x05D6F770>
>>> b.insert(b.root, BSTNode(18))
Left Node Value:18, Parent Value:20
Right Node Value:18, Parent Value:15
parent:18
<__main__.BSTNode object at 0x05D6F770>
>>> b.insert(b.root, BSTNode(22))
Right Node Value:22, Parent Value:20
Left Node Value:22, Parent Value:30
parent:22
<__main__.BSTNode object at 0x05D6F770>
>>> b.insert(b.root, BSTNode(35))
Right Node Value:35, Parent Value:20
Right Node Value:35, Parent Value:30
parent:35
<__main__.BSTNode object at 0x05D6F770>
>>> b.insert(b.root, BSTNode(9))
Left Node Value:9, Parent Value:20
Left Node Value:9, Parent Value:15
Left Node Value:9, Parent Value:10
parent:9
<__main__.BSTNode object at 0x05D6F770>
>>> b.insert(b.root, BSTNode(13))
Left Node Value:13, Parent Value:20
Left Node Value:13, Parent Value:15
Right Node Value:13, Parent Value:10
parent:13
<__main__.BSTNode object at 0x05D6F770>
>>> b.insert(b.root, BSTNode(11))
Left Node Value:11, Parent Value:20
Left Node Value:11, Parent Value:15
Right Node Value:11, Parent Value:10
Left Node Value:11, Parent Value:13
parent:11
<__main__.BSTNode object at 0x05D6F770>
>>> b.insert(b.root, BSTNode(12))
Left Node Value:12, Parent Value:20
Left Node Value:12, Parent Value:15
Right Node Value:12, Parent Value:10
Left Node Value:12, Parent Value:13
Right Node Value:12, Parent Value:11
parent:12
<__main__.BSTNode object at 0x05D6F770>
>>> b.min()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    b.min()
AttributeError: 'BST' object has no attribute 'min'
>>> b.min_node()
(<__main__.BSTNode object at 0x05D6FB70>, 9)
>>> b.max_node()
(<__main__.BSTNode object at 0x05D6FB90>, 35)
>>> b.insert(b.root, BSTNode(32))
Right Node Value:32, Parent Value:20
Right Node Value:32, Parent Value:30
Left Node Value:32, Parent Value:35
parent:32
<__main__.BSTNode object at 0x05D6F770>
>>> b.insert(b.root, BSTNode(40))
Right Node Value:40, Parent Value:20
Right Node Value:40, Parent Value:30
Right Node Value:40, Parent Value:35
parent:40
<__main__.BSTNode object at 0x05D6F770>
>>> b.insert(b.root, BSTNode(38))
Right Node Value:38, Parent Value:20
Right Node Value:38, Parent Value:30
Right Node Value:38, Parent Value:35
Left Node Value:38, Parent Value:40
parent:38
<__main__.BSTNode object at 0x05D6F770>
>>> b.insert(b.root, BSTNode(42))
Right Node Value:42, Parent Value:20
Right Node Value:42, Parent Value:30
Right Node Value:42, Parent Value:35
Right Node Value:42, Parent Value:40
parent:42
<__main__.BSTNode object at 0x05D6F770>
>>> b.max_node()
(<__main__.BSTNode object at 0x05D6FD70>, 42)
>>> b.find_min(b.root)
<__main__.BSTNode object at 0x05D6FB70>
>>> b.delete(b.root, 18)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    b.delete(b.root, 18)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 81, in delete
    parent.left = self.delete(parent.left, val)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 83, in delete
    parent.right = self.delete(parent.right, val)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 81, in delete
    parent.left = self.delete(parent.left, val)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 80, in delete
    elif val <= parent.value:
AttributeError: 'NoneType' object has no attribute 'value'
>>> 
========== RESTART: D:\SatyamSinha\DS Programs\BSTImplementation.py ==========
>>> b = BST()
>>> b.insert(None, BSTNode(20))
'Root value:20'
>>> b.insert(b.root, BSTNode(15))
Left Node Value:15, Parent Value:20
parent:15
<__main__.BSTNode object at 0x052EAF50>
>>> b.insert(b.root, BSTNode(30))
Right Node Value:30, Parent Value:20
parent:30
<__main__.BSTNode object at 0x052EAF50>
>>> b.insert(b.root, BSTNode(10))
Left Node Value:10, Parent Value:20
Left Node Value:10, Parent Value:15
parent:10
<__main__.BSTNode object at 0x052EAF50>
>>> b.delete(b.root, 10)
<__main__.BSTNode object at 0x052EAF50>
>>> b.root.value
20
>>> b.root.left.value
15
>>> b.root.left.left.value
10
>>> 
========== RESTART: D:\SatyamSinha\DS Programs\BSTImplementation.py ==========
>>> b = BST()
>>> b.insert(None, BSTNode(20))
'Root value:20'
>>> b.insert(b.root, BSTNode(15))
Left Node Value:15, Parent Value:20
parent:15
<__main__.BSTNode object at 0x060FF730>
>>> b.insert(b.root, BSTNode(30))
Right Node Value:30, Parent Value:20
parent:30
<__main__.BSTNode object at 0x060FF730>
>>> b.insert(b.root, BSTNode(10))
Left Node Value:10, Parent Value:20
Left Node Value:10, Parent Value:15
parent:10
<__main__.BSTNode object at 0x060FF730>
>>> b.delete(b.root, 10)
10
15
20
<__main__.BSTNode object at 0x060FF730>
>>> b.root.value
20
>>> b.root.left.value
15
>>> b.root.left.left.value
10
>>> 
========== RESTART: D:\SatyamSinha\DS Programs\BSTImplementation.py ==========
>>> b = BST()
>>> b.insert(None, BSTNode(20))
'Root value:20'
>>> b.insert(b.root, BSTNode(15))
Left Node Value:15, Parent Value:20
parent:15
<__main__.BSTNode object at 0x05E6F6F0>
>>> b.insert(b.root, BSTNode(30))
Right Node Value:30, Parent Value:20
parent:30
<__main__.BSTNode object at 0x05E6F6F0>
>>> b.insert(b.root, BSTNode(10))
Left Node Value:10, Parent Value:20
Left Node Value:10, Parent Value:15
parent:10
<__main__.BSTNode object at 0x05E6F6F0>
>>> b.delete(b.root, 10)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    b.delete(b.root, 10)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 82, in delete
    parent.left = self.delete(parent.left, val)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 82, in delete
    parent.left = self.delete(parent.left, val)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 97, in delete
    print(parent.value)
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.root.value
20
>>> b.root.left.value
15
>>> b.root.left.left.value
10
>>> 
========== RESTART: D:\SatyamSinha\DS Programs\BSTImplementation.py ==========
>>> b = BST()
>>> b.insert(None, BSTNode(20))
'Root value:20'
>>> b.insert(b.root, BSTNode(15))
Left Node Value:15, Parent Value:20
parent:15
<__main__.BSTNode object at 0x05A4F710>
>>> b.insert(b.root, BSTNode(30))
Right Node Value:30, Parent Value:20
parent:30
<__main__.BSTNode object at 0x05A4F710>
>>> b.insert(b.root, BSTNode(10))
Left Node Value:10, Parent Value:20
Left Node Value:10, Parent Value:15
parent:10
<__main__.BSTNode object at 0x05A4F710>
>>> b.delete(b.root, 10)
<__main__.BSTNode object at 0x05A4F710>
>>> b.root.value
20
>>> b.root.left.value
15
>>> b.root.left.left.value
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    b.root.left.left.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.root.left.left
>>> b = BST()
>>> b.insert(None, BSTNode(20))
'Root value:20'
>>> b.insert(None, BSTNode(15))
parent:15
<__main__.BSTNode object at 0x05A4FAD0>
>>> b.insert(None, BSTNode(18))
parent:18
<__main__.BSTNode object at 0x05A4F710>
>>> b.insert(None, BSTNode(10))
parent:10
<__main__.BSTNode object at 0x05A4FBD0>
>>> 
>>> b.insert(None, BSTNode(9))
parent:9
<__main__.BSTNode object at 0x05A4F6F0>
>>> b.insert(None, BSTNode(13))
parent:13
<__main__.BSTNode object at 0x05A4F4B0>
>>> b.insert(None, BSTNode(11))
parent:11
<__main__.BSTNode object at 0x05A4FAD0>
>>> b.insert(None, BSTNode(12))
parent:12
<__main__.BSTNode object at 0x05A4F710>
>>> b.insert(None, BSTNode(30))
parent:30
<__main__.BSTNode object at 0x05A4F770>
>>> b.insert(None, BSTNode(22))
parent:22
<__main__.BSTNode object at 0x05A4FBD0>
>>> 
>>> b.insert(None, BSTNode(35))
parent:35
<__main__.BSTNode object at 0x05A4F4B0>
>>> b.insert(None, BSTNode(32))
parent:32
<__main__.BSTNode object at 0x05A4FB30>
>>> b.insert(None, BSTNode(40))
parent:40
<__main__.BSTNode object at 0x05A4F710>
>>> b.insert(None, BSTNode(38))
parent:38
<__main__.BSTNode object at 0x05A4F770>
>>> b.insert(None, BSTNode(42))
parent:42
<__main__.BSTNode object at 0x05A4F6F0>
>>> b.delete(b.root, 18)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    b.delete(b.root, 18)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 82, in delete
    parent.left = self.delete(parent.left, val)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 81, in delete
    elif val < parent.value:
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.root.value
20
>>> b.root.left.value
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    b.root.left.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> 
========== RESTART: D:\SatyamSinha\DS Programs\BSTImplementation.py ==========
>>> b = BST()
>>> b.insert(None, BSTNode(20))
'Root value:20'
>>> b.insert(None, BSTNode(15))
parent:15
<__main__.BSTNode object at 0x05C6F8D0>
>>> b.insert(None, BSTNode(10))
parent:10
<__main__.BSTNode object at 0x05C6F530>
>>> b.root.value
20
>>> b.root.left
>>> b.delete(b.root, 20)
>>> b.root
<__main__.BSTNode object at 0x0591AF50>
>>> b.root.value
20
>>> b.insert(b.root, BSTNode(15))
Left Node Value:15, Parent Value:20
parent:15
<__main__.BSTNode object at 0x0591AF50>
>>> b.delete(b.root, 15)
<__main__.BSTNode object at 0x0591AF50>
>>> b.root.value
20
>>> b.root.left.value
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    b.root.left.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.traverse(b.root)
20,
>>> b.insert(b.root, BSTNode(15))
Left Node Value:15, Parent Value:20
parent:15
<__main__.BSTNode object at 0x0591AF50>
>>> b.insert(b.root, BSTNode(10))
Left Node Value:10, Parent Value:20
Left Node Value:10, Parent Value:15
parent:10
<__main__.BSTNode object at 0x0591AF50>
>>> b.insert(b.root, BSTNode(18))
Left Node Value:18, Parent Value:20
Right Node Value:18, Parent Value:15
parent:18
<__main__.BSTNode object at 0x0591AF50>
>>> b.delete(b.root, 18)
<__main__.BSTNode object at 0x0591AF50>
>>> b.root.left.right
>>> b.insert(b.root, BSTNode(18))
Left Node Value:18, Parent Value:20
Right Node Value:18, Parent Value:15
parent:18
<__main__.BSTNode object at 0x0591AF50>
>>> b.insert(b.root, BSTNode(19))
Left Node Value:19, Parent Value:20
Right Node Value:19, Parent Value:15
Right Node Value:19, Parent Value:18
parent:19
<__main__.BSTNode object at 0x0591AF50>
>>> b.delete(b.root, 18)
<__main__.BSTNode object at 0x0591AF50>
>>> b.root.left.right.value
19
>>> b.insert(b.root, BSTNode(13))
Left Node Value:13, Parent Value:20
Left Node Value:13, Parent Value:15
Right Node Value:13, Parent Value:10
parent:13
<__main__.BSTNode object at 0x0591AF50>
>>> b.insert(b.root, BSTNode(11))
Left Node Value:11, Parent Value:20
Left Node Value:11, Parent Value:15
Right Node Value:11, Parent Value:10
Left Node Value:11, Parent Value:13
parent:11
<__main__.BSTNode object at 0x0591AF50>
>>> b.insert(b.root, BSTNode(12))
Left Node Value:12, Parent Value:20
Left Node Value:12, Parent Value:15
Right Node Value:12, Parent Value:10
Left Node Value:12, Parent Value:13
Right Node Value:12, Parent Value:11
parent:12
<__main__.BSTNode object at 0x0591AF50>
>>> b.insert(b.root, BSTNode(9))
Left Node Value:9, Parent Value:20
Left Node Value:9, Parent Value:15
Left Node Value:9, Parent Value:10
parent:9
<__main__.BSTNode object at 0x0591AF50>
>>> b.delete(b.root, 10)
Find Min:11
<__main__.BSTNode object at 0x0591AF50>
>>> b.root.left.left.value
11
>>> b.delete(b.root, 12)
<__main__.BSTNode object at 0x0591AF50>
>>> b.traverse(b.root)
9,11,11,13,15,19,20,
>>> b.root.value
20
>>> b.root.left.value
15
>>> b.root.left.right.value
19
>>> b.root.left.left.value
11
>>> b.root.left.left.right.left.value
11
>>> b.delete(b.root, 19)
<__main__.BSTNode object at 0x0591AF50>
>>> b.root.left.right.value
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    b.root.left.right.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.delete(b.root, 15)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    b.delete(b.root, 15)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 82, in delete
    parent.left = self.delete(parent.left, val)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 94, in delete
    current = self.find_min(parent.right)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 72, in find_min
    while current.left:
AttributeError: 'NoneType' object has no attribute 'left'
>>> 
========== RESTART: D:\SatyamSinha\DS Programs\BSTImplementation.py ==========
>>> b = BST()
>>> b.insert(None, BSTNode(20))
'Root value:20'
>>> b.insert(b.root, BSTNode(15))
Left Node Value:15, Parent Value:20
parent:15
<__main__.BSTNode object at 0x063CF770>
>>> b.insert(b.root, BSTNode(19))
Left Node Value:19, Parent Value:20
Right Node Value:19, Parent Value:15
parent:19
<__main__.BSTNode object at 0x063CF770>
>>> b.insert(b.root, BSTNode(10))
Left Node Value:10, Parent Value:20
Left Node Value:10, Parent Value:15
parent:10
<__main__.BSTNode object at 0x063CF770>
>>> b.traverse(b.root)
10,15,19,20,
>>> b.delete(b.root, 19)
<__main__.BSTNode object at 0x063CF770>
>>> b.traverse(b.root)
10,15,20,
>>> b.delete(b.root, 15)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    b.delete(b.root, 15)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 82, in delete
    parent.left = self.delete(parent.left, val)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 95, in delete
    parent.value = current.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> 
========== RESTART: D:\SatyamSinha\DS Programs\BSTImplementation.py ==========
>>> b = BST()
>>> b.insert(None, BSTNode(20))
'Root value:20'
>>> b.insert(b.root, BSTNode(15))
Left Node Value:15, Parent Value:20
parent:15
<__main__.BSTNode object at 0x05A6F790>
>>> b.insert(b.root, BSTNode(10))
Left Node Value:10, Parent Value:20
Left Node Value:10, Parent Value:15
parent:10
<__main__.BSTNode object at 0x05A6F790>
>>> b.traverse(b.root)
10,15,20,
>>> b.delete(b.root, 15)
<__main__.BSTNode object at 0x05A6F790>
>>> b.traverse(b.root)
10,20,
>>> 
========== RESTART: D:\SatyamSinha\DS Programs\BSTImplementation.py ==========
>>> b = BST()
>>> b.insert(None, BSTNode(20))
'Root value:20'
>>> b.insert(b.root, BSTNode(10))
Left Node Value:10, Parent Value:20
parent:10
<__main__.BSTNode object at 0x05EDF730>
>>> b.insert(b.root, BSTNode(9))
Left Node Value:9, Parent Value:20
Left Node Value:9, Parent Value:10
parent:9
<__main__.BSTNode object at 0x05EDF730>
>>> b.insert(b.root, BSTNode(13))
Left Node Value:13, Parent Value:20
Right Node Value:13, Parent Value:10
parent:13
<__main__.BSTNode object at 0x05EDF730>
>>> b.insert(b.root, BSTNode(11))
Left Node Value:11, Parent Value:20
Right Node Value:11, Parent Value:10
Left Node Value:11, Parent Value:13
parent:11
<__main__.BSTNode object at 0x05EDF730>
>>> b.insert(b.root, BSTNode(12))
Left Node Value:12, Parent Value:20
Right Node Value:12, Parent Value:10
Left Node Value:12, Parent Value:13
Right Node Value:12, Parent Value:11
parent:12
<__main__.BSTNode object at 0x05EDF730>
>>> b.traverse(b.root)
9,10,11,12,13,20,
>>> b.root.left.right.value
13
>>> b.delete(b.root, 10)
Find Min:11
<__main__.BSTNode object at 0x05EDF730>
>>> b.traverse(b.root)
9,11,12,13,20,
>>> b.root.left.right.left.value
12
>>> 
========== RESTART: D:\SatyamSinha\DS Programs\BSTImplementation.py ==========
>>> b = BST()
>>> b.insert(None, BSTNode(15))
'Root value:15'
>>> b.insert(b.root, BSTNode(10))
Left Node Value:10, Parent Value:15
parent:10
<__main__.BSTNode object at 0x05F0AF10>
>>> b.insert(b.root, BSTNode(8))
Left Node Value:8, Parent Value:15
Left Node Value:8, Parent Value:10
parent:8
<__main__.BSTNode object at 0x05F0AF10>
>>> b.insert(b.root, BSTNode(12))
Left Node Value:12, Parent Value:15
Right Node Value:12, Parent Value:10
parent:12
<__main__.BSTNode object at 0x05F0AF10>
>>> b.insert(b.root, BSTNode(11))
Left Node Value:11, Parent Value:15
Right Node Value:11, Parent Value:10
Left Node Value:11, Parent Value:12
parent:11
<__main__.BSTNode object at 0x05F0AF10>
>>> b.insert(b.root, BSTNode(8))
Left Node Value:8, Parent Value:15
Left Node Value:8, Parent Value:10
Left Node Value:8, Parent Value:8
parent:8
<__main__.BSTNode object at 0x05F0AF10>
>>> b.insert(b.root, BSTNode(6))
Left Node Value:6, Parent Value:15
Left Node Value:6, Parent Value:10
Left Node Value:6, Parent Value:8
Left Node Value:6, Parent Value:8
parent:6
<__main__.BSTNode object at 0x05F0AF10>
>>> b.traverse(b.root)
6,8,8,10,11,12,15,
>>> b.delete(b.root, 8)
<__main__.BSTNode object at 0x05F0AF10>
>>> b.traverse(b.root)
6,8,10,11,12,15,
>>> b.inorder_successor(b.root, 10)
Find Min:11
11
>>> b.inorder_successor(b.root, 6)
8
>>> b.inorder_successor(b.root, 12)
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    b.inorder_successor(b.root, 12)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 141, in inorder_successor
    elif current.value > ancestor.right:
TypeError: '>' not supported between instances of 'int' and 'BSTNode'
>>> 
========== RESTART: D:\SatyamSinha\DS Programs\BSTImplementation.py ==========
>>> b = BST()
>>> b.insert(None, BSTNode(15))
'Root value:15'
>>> b.insert(b.root, BSTNode(10))
Left Node Value:10, Parent Value:15
parent:10
<__main__.BSTNode object at 0x0524AEF0>
>>> b.insert(b.root, BSTNode(12))
Left Node Value:12, Parent Value:15
Right Node Value:12, Parent Value:10
parent:12
<__main__.BSTNode object at 0x0524AEF0>
>>> b.insert(b.root, BSTNode(11))
Left Node Value:11, Parent Value:15
Right Node Value:11, Parent Value:10
Left Node Value:11, Parent Value:12
parent:11
<__main__.BSTNode object at 0x0524AEF0>
>>> b.traverse(b.root)
10,11,12,15,
>>> b.inorder_successor(b.root, 12)
15
>>> b.inorder_successor(b.root, 15)
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    b.inorder_successor(b.root, 15)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 143, in inorder_successor
    return successor.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.insert(b.root, BSTNode(20))
Right Node Value:20, Parent Value:15
parent:20
<__main__.BSTNode object at 0x0524AEF0>
>>> b.insert(b.root, BSTNode(18))
Right Node Value:18, Parent Value:15
Left Node Value:18, Parent Value:20
parent:18
<__main__.BSTNode object at 0x0524AEF0>
>>> b.traverse(b.root)
10,11,12,15,18,20,
>>> b.inorder_successor(b.root, 15)
Find Min:18
18
>>> b.inorder_successor(b.root, 18)
20
>>> 
========== RESTART: D:\SatyamSinha\DS Programs\BSTImplementation.py ==========
>>> b = BST()
>>> b.insert(None, BSTNode(15))
'Root value:15'
>>> b.insert(b.root, BSTNode(10))
Left Node Value:10, Parent Value:15
parent:10
<__main__.BSTNode object at 0x05F8F8B0>
>>> b.insert(b.root, BSTNode(12))
Left Node Value:12, Parent Value:15
Right Node Value:12, Parent Value:10
parent:12
<__main__.BSTNode object at 0x05F8F8B0>
>>> b.insert(b.root, BSTNode(11))
Left Node Value:11, Parent Value:15
Right Node Value:11, Parent Value:10
Left Node Value:11, Parent Value:12
parent:11
<__main__.BSTNode object at 0x05F8F8B0>
>>> b.insert(b.root, BSTNode(8))
Left Node Value:8, Parent Value:15
Left Node Value:8, Parent Value:10
parent:8
<__main__.BSTNode object at 0x05F8F8B0>
>>> b.insert(b.root, BSTNode(6))
Left Node Value:6, Parent Value:15
Left Node Value:6, Parent Value:10
Left Node Value:6, Parent Value:8
parent:6
<__main__.BSTNode object at 0x05F8F8B0>
>>> b.inorder_predecessor(6)
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    b.inorder_predecessor(6)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 176, in inorder_predecessor
    return successor.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.inorder_predecessor(8)
Find Max:6
6
>>> b.inorder_predecessor(10)
Find Max:8
8
>>> b.delete(b.root, 8)
<__main__.BSTNode object at 0x05F8F8B0>
>>> b.traverse(b.root)
6,10,11,12,15,
>>> b.delete(b.root, 6)
<__main__.BSTNode object at 0x05F8F8B0>
>>> b.traverse(b.root)
10,11,12,15,
>>> b.inorder_predecessor(10)
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    b.inorder_predecessor(10)
  File "D:\SatyamSinha\DS Programs\BSTImplementation.py", line 176, in inorder_predecessor
    return successor.value
AttributeError: 'NoneType' object has no attribute 'value'
>>> b.inorder_predecessor(11)
10
>>> b.insert(b.root, BSTNode(20))
Right Node Value:20, Parent Value:15
parent:20
<__main__.BSTNode object at 0x05F8F8B0>
>>> b.insert(b.root, BSTNode(25))
Right Node Value:25, Parent Value:15
Right Node Value:25, Parent Value:20
parent:25
<__main__.BSTNode object at 0x05F8F8B0>
>>> b.insert(b.root, BSTNode(18))
Right Node Value:18, Parent Value:15
Left Node Value:18, Parent Value:20
parent:18
<__main__.BSTNode object at 0x05F8F8B0>
>>> b.insert(b.root, BSTNode(28))
Right Node Value:28, Parent Value:15
Right Node Value:28, Parent Value:20
Right Node Value:28, Parent Value:25
parent:28
<__main__.BSTNode object at 0x05F8F8B0>
>>> b.traverse(b.root)
10,11,12,15,18,20,25,28,
>>> b.inorder_predecessor(18)
15
>>> b.inorder_predecessor(20)
Find Max:18
18
>>> b.inorder_predecessor(28)
25
>>> b.inorder_predecessor(25)
20
>>> b.inorder_predecessor(30)
>>> 
