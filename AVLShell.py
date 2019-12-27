Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: G:/ProgramsPython/Algorithms/AVLTree.py ==============
>>> bst = BST()
>>> bst.insert(None, 3)
<__main__.Node object at 0x04169A10>
>>> bst.root
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    bst.root
AttributeError: 'BST' object has no attribute 'root'
>>> 
============== RESTART: G:/ProgramsPython/Algorithms/AVLTree.py ==============
>>> avl = AVLTree()
>>> root = None
>>> root = avl.insert(root, 13)
>>> root.val
13
>>> root.height
0
>>> avl.insert(root, 10)
<__main__.Node object at 0x039699F0>
>>> avl.insert(root, 15)
<__main__.Node object at 0x039699F0>
>>> avl.insert(root, 16)
<__main__.Node object at 0x039699F0>
>>> root.left.val
10
>>> root.left.left.val
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    root.left.left.val
AttributeError: 'NoneType' object has no attribute 'val'
>>> root.left.height
0
>>> root.height
2
>>> root.right.val
15
>>> avl.inorder(root)
10 0
13 2
15 1
16 0
>>> 
============== RESTART: G:/ProgramsPython/Algorithms/AVLTree.py ==============
>>> avl = AVLTree()
>>> root = None
>>> root = avl.insert(root, 13)
>>> root.balance
0
>>> avl.insert(root, 10)
<__main__.Node object at 0x03AE7E50>
>>> root.balance
1
>>> root.left.balance
0
>>> avl.insert(root, 15)
<__main__.Node object at 0x03AE7E50>
>>> avl.insert(root, 16)
<__main__.Node object at 0x03AE7E50>
>>> root.right.balance
-1
>>> root.right.right.balance
0
>>> root.balance
-1
>>> root.left.balance
0
>>> root.height
2
>>> root.right.height
1
>>> root.right.right.height
0
>>> 
============== RESTART: G:/ProgramsPython/Algorithms/AVLTree.py ==============
>>> avl = AVLTree()
>>> root = avl.insert(None, 30)
>>> root = avl.insert(None, 10)
>>> root = avl.insert(root, 20)
>>> root = avl.insert(root, 30)
>>> root = avl.insert(root, 40)
>>> root = avl.insert(root, 50)
>>> avl.inorder(root)
10 2
20 3
30 2
40 1
50 0
>>> root = avl.insert(root, 25)
>>> avl.inorder(root)
10 2
20 3
25 0
30 1
40 2
50 0
>>> 
============== RESTART: G:/ProgramsPython/Algorithms/AVLTree.py ==============
>>> avl = AVLTree()
>>> root = avl.insert(None, 30)
>>> root = avl.insert(None, 10)
>>> root = avl.insert(root, 20)
>>> root = avl.insert(root, 30)
>>> root = avl.insert(root, 40)
>>> root = avl.insert(root, 50)
>>> avl.inorder(root)
10 0 -2
20 4 -4
30 3 -2
40 4 -1
50 0 0
>>> root.val
40
>>> root.left.val
20
>>> root.left.left.val
10
>>> root.left.right.val
30
>>> root.right.val
50
>>> 
============== RESTART: G:/ProgramsPython/Algorithms/AVLTree.py ==============
>>> avl = AVLTree()
>>> root = avl.insert(None, 10)
>>> root = avl.insert(root, 20)
>>> root = avl.insert(root, 30)
>>> root = avl.insert(root, 40)
>>> root = avl.insert(root, 50)
>>> avl.inorder(root)
10 0 -2
20 2 -1
30 0 -2
40 1 -1
50 0 0
>>> root.val
20
>>> root.right.val
40
>>> 
============== RESTART: G:/ProgramsPython/Algorithms/AVLTree.py ==============
>>> avl = AVLTree()
>>> root = avl.insert(None, 10)
>>> root = avl.insert(root, 20)
>>> root = avl.insert(root, 30)
>>> root = avl.insert(root, 40)
>>> root = avl.insert(root, 50)
>>> avl.inorder(root)
10 0 0
20 2 -1
30 0 0
40 1 0
50 0 0
>>> root = avl.insert(root, 25)
>>> avl.inorder(root)
10 0 0
20 2 -1
25 0 0
30 1 1
40 3 2
50 0 0
>>> root.val
40
>>> root.left.val
20
>>> root.right.val
50
>>> root.left.right.val
30
>>> root.left.left.val
10
>>> root.left.right.left
<__main__.Node object at 0x035E7F70>
>>> root.left.right.left.val
25
>>> 
