Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: G:\ProgramsPython\Algorithms\AVLTree.py ==============
>>> avl = AVLTree()
>>> root = None
>>> nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
>>> for num in nums:
	root = avl.insert(root, num)

	
>>> root.val
9
>>> avl.inorder(root)
-1 0 0
0 1 1
1 2 0
2 0 0
5 1 0
6 0 0
9 3 1
10 1 -1
11 0 0
>>> 
============== RESTART: G:\ProgramsPython\Algorithms\AVLTree.py ==============
>>> avl = AVLTree()
>>> root = None
>>> nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
>>> for num in nums:
	root = avl.insert(root, num)

	
>>> avl.preorder(root)
9 3 1
1 2 0
0 1 1
-1 0 0
5 1 0
2 0 0
6 0 0
10 1 -1
11 0 0
>>> avl.avl_delete(root, 10)
<__main__.Node object at 0x03788ED0>
>>> avl.preorder(root)
9 4 -1
1 2 0
0 1 1
-1 0 0
5 1 0
2 0 0
6 0 0
11 3 1
>>> root.val
9
>>> root.right.val
11
>>> root.right.left.val
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    root.right.left.val
AttributeError: 'NoneType' object has no attribute 'val'
>>> root.right.right.val
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    root.right.right.val
AttributeError: 'NoneType' object has no attribute 'val'
>>> root.right.height
3
>>> 
============== RESTART: G:\ProgramsPython\Algorithms\AVLTree.py ==============
>>> avl = AVLTree()
>>> root = None
>>> nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
>>> for num in nums:
	root = avl.insert(root, num)

	
>>> avl.preorder(root)
9 3 1
1 2 0
0 1 1
-1 0 0
5 1 0
2 0 0
6 0 0
10 1 -1
11 0 0
>>> avl.avl_delete(root, 10)
<__main__.Node object at 0x041C8F70>
>>> avl.preorder(root)
9 4 -1
1 2 0
0 1 1
-1 0 0
5 1 0
2 0 0
6 0 0
11 3 1
>>> 
============== RESTART: G:\ProgramsPython\Algorithms\AVLTree.py ==============
>>> avl = AVLTree()
>>> root = None
>>> nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
>>> for num in nums:
	root = avl.insert(root, num)

	
>>> avl.preorder(root)
9 3 1
1 2 0
0 1 1
-1 0 0
5 1 0
2 0 0
6 0 0
10 1 -1
11 0 0
>>> avl.avl_delete(root, 10)
<__main__.Node object at 0x03888F50>
>>> avl.preorder(root)
9 4 -1
1 2 0
0 1 1
-1 0 0
5 1 0
2 0 0
6 0 0
11 3 1
>>> 
============== RESTART: G:\ProgramsPython\Algorithms\AVLTree.py ==============
>>> avl = AVLTree()
>>> root = None
>>> nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
>>> for num in nums:
	root = avl.insert(root, num)

	
>>> avl.preorder(root)
9 3 1
1 2 0
0 1 1
-1 0 0
5 1 0
2 0 0
6 0 0
10 1 -1
11 0 0
>>> avl.avl_delete(root, 10)
<__main__.Node object at 0x03DAA0D0>
>>> avl.preorder(root)
9 2 1
5 1 0
2 0 0
6 0 0
11 0 0
>>> avl = AVLTree()
>>> root = None
>>> nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
>>> for num in nums:
	root = avl.insert(root, num)

	
>>> avl.preorder(root)
9 3 1
1 2 0
0 1 1
-1 0 0
5 1 0
2 0 0
6 0 0
10 1 -1
11 0 0
>>> avl.avl_delete(root, 10)
<__main__.Node object at 0x03DAA510>
>>> avl.preorder(root)
9 2 1
5 1 0
2 0 0
6 0 0
11 0 0
>>> avl.inorder(root)
2 0 0
5 1 0
6 0 0
9 2 1
11 0 0
>>> 
============== RESTART: G:\ProgramsPython\Algorithms\AVLTree.py ==============
>>> avl = AVLTree()
>>> root = None
>>> nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
>>> for num in nums:
	root = avl.insert(root, num)

	
>>> avl.preorder(root)
9 3 1
1 2 0
0 1 1
-1 0 0
5 1 0
2 0 0
6 0 0
10 1 -1
11 0 0
>>> avl.avl_delete(root, 10)
LL rotation:
<__main__.Node object at 0x03D6A0F0>
>>> avl.preorder(root)
9 2 1
5 1 0
2 0 0
6 0 0
11 0 0
>>> 
============== RESTART: G:\ProgramsPython\Algorithms\AVLTree.py ==============
>>> 
============== RESTART: G:\ProgramsPython\Algorithms\AVLTree.py ==============
>>> avl = AVLTree()
>>> root = None
>>> nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
>>> for num in nums:
	root = avl.insert(root, num)

	
>>> avl.preorder(root)
9 3 1
1 2 0
0 1 1
-1 0 0
5 1 0
2 0 0
6 0 0
10 1 -1
11 0 0
>>> avl.avl_delete(root, 10)
Right half of tree: Value greater than parent.val
Case2: Presence of right child only
Update Height 11 0
Updated Height 11 0
Update balance factor 11 0
Updated balance factor 11 0
Update Height 9 3
Updated Height 9 3
Update balance factor 9 1
Updated balance factor 9 2
LL rotation: 9
<__main__.Node object at 0x040E8070>
>>> avl.preorder(root)
9 2 1
5 1 0
2 0 0
6 0 0
11 0 0
>>> 
============== RESTART: G:\ProgramsPython\Algorithms\AVLTree.py ==============
>>> avl = AVLTree()
>>> root = None
>>> nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
>>> for num in nums:
	root = avl.insert(root, num)

	
1
>>> root.val
9
>>> y
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> avl.preorder(root)
9 3 1
1 2 0
0 1 1
-1 0 0
5 1 0
2 0 0
6 0 0
10 1 -1
11 0 0
>>> avl.avl_delete(root, 10)
Right half of tree: Value greater than parent.val
Case2: Presence of right child only
Update Height 11 0
Updated Height 11 0
Update balance factor 11 0
Updated balance factor 11 0
Update Height 9 3
Updated Height 9 3
Update balance factor 9 1
Updated balance factor 9 2
LL rotation: 9
1
<__main__.Node object at 0x03C490B0>
>>> avl.preorder(root)
9 2 1
5 1 0
2 0 0
6 0 0
11 0 0
>>> avl = AVLTree()
>>> root = None
>>> nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
>>> for num in nums:
	root = avl.insert(root, num)

	
1
>>> avl.preorder(root)
9 3 1
1 2 0
0 1 1
-1 0 0
5 1 0
2 0 0
6 0 0
10 1 -1
11 0 0
>>> root = avl.avl_delete(root, 10)
Right half of tree: Value greater than parent.val
Case2: Presence of right child only
Update Height 11 0
Updated Height 11 0
Update balance factor 11 0
Updated balance factor 11 0
Update Height 9 3
Updated Height 9 3
Update balance factor 9 1
Updated balance factor 9 2
LL rotation: 9
1
>>> avl.preorder(root)
1 3 -1
0 1 1
-1 0 0
9 2 1
5 1 0
2 0 0
6 0 0
11 0 0
>>> # root wasn't updated earlier so I kept
>>> # getting root as 9. Now, setting
>>> # root = avl.avl_delete(root, 10), thus,
>>> # when accessing preorder(root) I get correct output for the tree nodes.
>>> 
