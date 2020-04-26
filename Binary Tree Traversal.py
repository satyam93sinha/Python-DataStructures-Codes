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
    
    def inorderTraversalIterative(self, root: TreeNode) -> List[int]:
        """
        We need to use a Data Structure which gives us recently visited nodes thus, we use STACK(LIFO). There can be a time when stack
        is empty but we haven't visited the whole tree/ all the nodes so we iterate until the stack is empty or node!=None.
        If node is None it means left or right leaf is reached and we need to trace back to recently visited node's parent which isn't
        yet visited or whose right or left leaves are still unvisited. Keep adding them to the stack and popping them if node is None.
        """
        stack = list()
        inorder_traversal = list()
        node = root
        while node or len(stack):
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                inorder_traversal.append(node.val)
                node = node.right
        return inorder_traversal
        
                
                
                
