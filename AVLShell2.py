Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: G:\ProgramsPython\Algorithms\AVLTree.py ==============
>>> avl = AVLTree()
>>> root = None
>>> root = avl.insert(root, 10)
>>> root.val
10
>>> root
<__main__.Node object at 0x03DBD5D0>
>>> root.height
0
>>> root.balance
0
>>> root.left
>>> root = avl.insert(root, 20)
>>> root.val
10
>>> root
<__main__.Node object at 0x03DBD5D0>
>>> root.height
1
>>> root.balance
-1
>>> root.right.val
20
>>> root.right.height
0
>>> root.right.balance
0
>>> root = avl.insert(root, 30)
>>> root.height
1
>>> root.val
20
>>> root.balance
0
>>> root.right.val
30
>>> root.right.height
0
>>> root.right.balance
0
>>> print(root.left.val, root.left.height,
	  root.left.balance)
10 0 0
>>> root = avl.insert(root, 40)
>>> print(root.val, root.height, root.balance)
20 2 -1
>>> print(root.left.val, root.left.height,
	  root.left.balance)
10 0 0
>>> print(root.right.val, root.right.height,
	  root.right.balance)
30 1 -1
>>> print(root.right.right.val,
	  root.right.right.height,
	  root.right.right.balance)
40 0 0
>>> root = avl.insert(root, 40)
>>> avl.inorder(root)
10 0 0
20 2 -1
30 0 0
40 1 0
40 0 0
>>> avl2 = AVLTree()
>>> root2 = None
>>> root2 = avl2.insert(root2, 10)
>>> root2 = avl2.insert(root2, 20)
>>> root2 = avl2.insert(root2, 30)
>>> root2 = avl2.insert(root2, 40)
>>> root2 = avl2.insert(root2, 50)
>>> avl2.inorder(root2)
10 0 0
20 2 -1
30 0 0
40 1 0
50 0 0
>>> print(root.val, root.height, root.balance)
20 2 -1
>>> print(root2.val, root2.height, root2.balance)
20 2 -1
>>> print(root2.right.val,
	  root2.right.height,
	  root2.right.balance)
40 1 0
>>> print(root2.right.right.val,
	  root2.right.right.height,
	  root2.right.right.balance)
50 0 0
>>> print(root2.right.left.val,
	  root2.right.left.height,
	  root2.right.left.balance)
30 0 0
>>> print(root2.left.val,
	  root2.left.height,
	  root2.left.balance)
10 0 0
>>> root2 = avl2.insert(root2, 25)
>>> avl2.inorder(root2)
10 0 0
20 2 -1
25 0 0
30 1 1
40 3 2
50 0 0
>>> print(root2.val, root2.height, root2.balance)
40 3 2
>>> 
============== RESTART: G:\ProgramsPython\Algorithms\AVLTree.py ==============
>>> avl = AVLTree()
>>> root = None
>>> root = avl.insert(root, 10)
>>> root = avl.insert(root, 20)
>>> root = avl.insert(root, 30)
>>> root = avl.insert(root, 40)
>>> root = avl.insert(root, 50)
>>> root = avl.insert(root, 25)

>>> avl.inorder(root)
10 0 0
20 1 0
25 0 0
30 2 0
40 1 -1
50 0 0
>>> print(root.val, root.height, root.balance)
30 2 0
>>> 
============== RESTART: G:\ProgramsPython\Algorithms\AVLTree.py ==============
>>> 
