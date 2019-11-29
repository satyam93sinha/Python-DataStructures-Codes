class Node:
    def __init__(self, node):
        self.value = node
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.queue = []
    def traverse_LOT(self, root):
        """Level Order Traversal"""
        if root == None:
            return -1
        else:
            self.queue.append(root)
            while len(self.queue)>0:
                print(self.queue[0].value)
                node = self.queue.pop(0)
                if node.left:
                    self.queue.append(node.left)
                if node.right:
                    self.queue.append(node.right)

    def preorder_traversal_recur(self, root):
        if root:
            print(root.value, end = ", ")
            self.preorder_traversal_recur(root.left)
            self.preorder_traversal_recur(root.right)
        else:
            return

    def postorder_traversal_recur(self, root):
        if root:
            self.postorder_traversal_recur(root.left)
            self.postorder_traversal_recur(root.right)
            print(root.value, end = ",")
        else:
            return

    def inorder_traversal_recur(self, root):
        if root:
            self.inorder_traversal_recur(root.left)
            print(root.value, end=',')
            self.inorder_traversal_recur(root.right)
        else:
            return
        
                
                
                
