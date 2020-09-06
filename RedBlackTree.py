class RBTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.color = "RED"

class RBTree:
    """Properties:
        1. Root node is BLACK
        2. No RED-RED parent-child relationship
        3. Number of BLACK nodes from root to any leaf stays same,
           i.e., black height never changes from root-leaf
        4. Longest path of root to leaf = 2*shortest path of root to leaf
    """
    def __init__(self):
        self.TNULL = RBTreeNode(None)
        self.TNULL.color = "BLACK"
        self.root = self.TNULL

    def insert(self, key):
        # A RBTreeNode is created
        node = RBTreeNode(key)
        # RBTreeNode's left and right is set to self.TNULL
        node.left = self.TNULL
        node.right = self.TNULL
        # if self.root is self.TNULL, i.e., null node, set current node as root
        if self.root == self.TNULL:
            print("self.root==self.TNULL:", self.root.val)
            self.root = node
            node.color = "BLACK"
            return
        else:
            # iterating to check parent and place for node's insertion
            parent = None
            child = self.root
            while child != self.TNULL:
                parent = child
                if node.val < child.val:
                    child = child.left
                elif node.val > child.val:
                    child = child.right
                else:
                    # avoiding duplicacy
                    return
            # found parent node and position for node's insertion
            node.parent = parent
            if node.val < parent.val:
                parent.left = node
            elif node.val > parent.val:
                parent.right = node
            # node is direct child of root node, it is assumed to be balanced
            if node.parent.parent == None:
                return
            else:
                self.fix_insert(node)
                
    def fix_insert(self, node):
        while node.parent.color == "RED":
            # node.parent is a RIGHT node
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                # uncle's color is RED
                if uncle.color == "RED":
                    uncle.color = "BLACK"
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    # uncle's color is BLACK or uncle is None, perform rotation
                    # current node is LEFT node, RL rotation
                    if node == node.parent.left:
                        node = node.parent
                        self.ll_rotation(node)
                    # RIGHT node, RR rotation, switch colors if RR or LL Rotation
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.rr_rotation(node.parent.parent)
            # node.parent is a LEFT node
            else:
                uncle = node.parent.parent.right
                # uncle's color is RED
                if uncle.color == "RED":
                    uncle.color = "BLACK"
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                # uncle's color is BLACK or uncle is None, perform rotation
                else:
                    # current node is RIGHT node, LR rotation
                    if node == node.parent.right:
                        node = node.parent
                        self.rr_rotation(node)
                    # LEFT node, LL Rotation, switch colors if RR or LL Rotation
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.ll_rotation(node.parent.parent)
            if node == self.root:
                break
        self.root.color = "BLACK"

    def ll_rotation(self, z):
        '''       z
                 / \
                y  T4
               / \
              x  T3
             / \
            T1 T2
        '''
        y = z.left
        T3 = y.right
        # Rotation:
        # setting T3 to z's left, at correct position
        z.left = T3
        if T3 != self.TNULL:
            T3.parent = z
        # setting y as current root, checking z is ROOT, RIGHT or LEFT node of it's PARENT
        y.parent = z.parent
        # z is a ROOT node
        if z.parent == None:
            self.root = y
        # z is a RIGHT node
        elif z == z.parent.right:
            z.parent.right = y
        # z is a LEFT node
        else:
            z.parent.left = y
        # setting z to y's right
        y.right = z
        z.parent = y

    def rr_rotation(self, z):
        '''      z
                / \
               T1  y
                  / \
                 T2  x
                    / \
                   T3 T4
        '''
        y = z.right
        T2 = y.left
        # Rotation:
        # setting T2 at its correct place
        z.right = T2
        if T2 != self.TNULL:
            T2.parent = z
        # setting y as current root, checking z is ROOT, RIGHT or LEFT node of it's PARENT
        # z is a ROOT node
        if z.parent == None:
            self.root = y
        # z is RIGHT node
        elif z == z.parent.right:
            z.parent.right = y
        # z is LEFT node
        else:
            z.parent.left = y
        y.parent = z.parent
        # setting z at its correct position
        y.left = z
        z.parent = y

    def inorder(self, root):
        if root == None:
            return root
        else:
            self.inorder(root.left)
            print("{}->{}".format(root.val, root.color), end=', ')
            self.inorder(root.right)
