class Node:
    def __init__(self, node):
        self.val = node
        self.left = None
        self.right = None
        self.height = 0
        self.balance = 0

class AVLTree:
    
    def getHeight(self, root):
        if not root:
            return -1
        return root.height
    
    def insert(self, root, node):
        if root == None:
            root = Node(node)
        elif node < root.val:
            root.left = self.insert(root.left, node)
        else:
            root.right = self.insert(root.right, node)

        # Step-2: Update height of parent node/ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        # Step-3: Get balance factor, balance factor = left_height-right_height
        root.balance = self.getHeight(root.left)-self.getHeight(root.right)
        # Step-4: Check if balance factor falls in LL, RR, LR or RL rotation
        # Step-5: Perform the rotations
        # Case1: LL (Left Left rotation): bf>1 and node lies left of root.left
        # bcoz LL says Left of Left of root node
        """     A
               /
              B
             /
            C
        """
        if root.balance>1 and node<root.left.val:
            return self.ll_rotation(root)
        # Case2: RR(Right Right rotation): bf<-1 and node lies right of root.right
        # bcoz RR says Right of Right of root node
        #"""   A
        #       \
        #        B
        #         \
        #          C
        #"""
        elif root.balance<-1 and node>root.right.val:
            return self.rr_rotation(root)
        # Case3: LR(Left Right rotation): bf>1 and node lies right of root.left
        # bcoz LR says Left of Right of root node
        #"""    A
        #      /
        #      B
        #      \
        #       C
        #"""
        elif root.balance>1 and node>root.left.val:
            root.left = self.rr_rotation(root.left)
            return self.ll_rotation(root)
        # Case4: RL(Right Left rotation): bf<-1 and node lies left of root.right
        # bcoz RL says Right of Left of root node
        #"""   A
        #       \
        #        B
        #       /
        #      C
        #"""
        elif root.balance<-1 and node<root.right.val:
            root.right = self.ll_rotation(root.right)
            return self.rr_rotation(root)

        return root

    def ll_rotation(self, z):
        """   z
             / \
            y   T4
           / \
          x   T3
         / \
        T1  T2
        """
        y = z.left
        T3 = y.right
        # Rotation-
        y.right = z
        z.left = T3
        # Update Heights of z, y bcoz changes occurred at these nodes
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        z.balance = self.getHeight(z.left)-self.getHeight(z.right)
        y.balance = self.getHeight(y.left)-self.getHeight(y.right)
        # Return root
        print(y.val)
        return y

    def rr_rotation(self, z):
        """  z
            / \
           T1  y
              / \
             T2  x
                / \
               T3  T4
        """
        y = z.right
        T2 = y.left
        # Rotation-
        y.left = z
        z.right = T2
        # Update Heights of z, y bcoz changes occurred at these nodes
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        z.balance = self.getHeight(z.left)-self.getHeight(z.right)
        y.balance = self.getHeight(y.left)-self.getHeight(y.right)
        # Return root
        return y
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, root.height, root.balance)
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.val, root.height,
                  root.balance)
            self.preorder(root.left)
            self.preorder(root.right)

    def find_min(self, parent):
        if parent:
            current = parent
            while current.left:
                current = current.left
            return current

    def avl_delete(self, parent, value):
        if not parent:
            print('Parent is None')
            return parent
        elif value<parent.val:
            print('Left half of tree: Value less than parent.val')
            parent.left = self.avl_delete(parent.left, value)
        elif value>parent.val:
            print('Right half of tree: Value greater than parent.val')
            parent.right = self.avl_delete(parent.right, value)
        # Performing delete operation
        else:
            # Case1: no child/leaf node
            if parent.left==None and parent.right==None:
                print('Case1: Leaf Node')
                parent = None
            # Case2: when only right child is present
            elif parent.left==None:
                print('Case2: Presence of right child only')
                parent = parent.right
            # Case3: when only left child is present
            elif parent.right==None:
                print('Case3: Presence of left child only')
                parent = parent.left
            # Case4: both the left and right children are present
            elif parent.right and parent.left:
                print('Case4: Right and Left children are present')
                min_ = self.find_min(parent.right)
                parent.val = min_.val
                parent.right = self.avl_delete(parent.right, min_.val)
        # Update Height
        print("Update Height", parent.val, parent.height)
        parent.height = 1 + max(self.getHeight(parent.left), self.getHeight(parent.right))
        print("Updated Height", parent.val, parent.height)
        # Update balance factor
        print("Update balance factor", parent.val, parent.balance)
        parent.balance = self.getHeight(parent.left)-self.getHeight(parent.right)
        print("Updated balance factor", parent.val, parent.balance)
        # Perform rotations-
        
        # Case1: LL Rotation: Left-Left of root rotation
        if parent.balance>1 and parent.left.balance>=0:
            print('LL rotation:', parent.val)
            return self.ll_rotation(parent)
        # Case2: RR rotation: Right-Right of root rotation
        elif parent.balance<-1 and parent.right.balance<=0:
            print('RR rotation:')
            return self.rr_rotation(parent)
        # Case3: LR rotation: Left-Right of root rotation
        elif parent.balance>1 and parent.left.balance<0:
            print('LR rotation:')
            parent.left = self.rr_rotation(parent.left)
            return self.ll_rotation(parent)
        # Case4: RL rotation: Right-Left of root rotation
        elif parent.balance<-1 and parent.right.balance>0:
            print("RL rotation:")
            parent.right = self.ll_rotation(parent.right)
            return self.rr_rotation(parent)
        return parent
