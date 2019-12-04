class BSTNode:
    def __init__(self, node = None):
        self.value = node
        self.left = None
        self.right = None

class BST:
    def __init__(self, root = None):
        # instance variable root pointing to root node
        self.root = root

    def insert(self, parent, node):
        if self.root == None:
            self.root = node
            return "Root value:{}".format(self.root.value)
        # when parent==None and root is not, parent can be set to node during recursion.
        elif parent == None and self.root:
            parent = node
            print("parent:{}".format(parent.value))
        elif node.value<=parent.value:
            print("Left Node Value:{}, Parent Value:{}".format(node.value, parent.value))
            parent.left = self.insert(parent.left, node)
        else:
            print("Right Node Value:{}, Parent Value:{}".format(node.value, parent.value))
            parent.right = self.insert(parent.right, node)
        return parent

    def min_node(self):
        if self.root == None:
            return "No elements in BST"
        else:
            current = self.root
            while current.left:
                current = current.left
            return (current, current.value)

    def max_node(self):
        if self.root == None:
            return "No elements in BST"
        else:
            current = self.root
            while current.right:
                current = current.right
            return (current, current.value)

    def insert_iter(self, node):
        if self.root == None:
            self.root = node
            return "Root value:{}".format(self.root.value)
        else:
            current = self.root
            previous = None
            while current:
                previous = current
                print("Current:{}, Node:{}".format(current.value, node.value))
                if current.value >= node.value:
                    current = current.left
                elif current.value < node.value:
                    current = current.right
            if node.value<=previous.value:
                previous.left = node
                print("Previous Left", previous.left.value)
            else:
                previous.right = node
                print("Previous Right", previous.right.value)

    def find(self, value):
        if self.root:
            current = self.root
            previous = None
            while current:
                previous = current
                if value < current.value:
                    current = current.left
                elif value > current.value:
                    current = current.right
                elif value == current.value:
                    return current
            return None

    def find_min(self, parent):
        if parent==None:
            return parent
        else:
            current = parent
            while current.left:
                if current.value <= parent.value:
                    current = current.left
            print("Find Min:{}".format(current.value))
            return current

    def delete(self, parent, val):
        if parent==None:
            return parent
        elif val < parent.value:
            parent.left = self.delete(parent.left, val)
        elif val > parent.value:
            parent.right = self.delete(parent.right, val)
        else:
            # no child
            if parent.left==None and parent.right==None:
                parent = None
            # only left/right child present
            elif parent.left == None:
                parent = parent.right
            elif parent.right == None:
                parent = parent.left
            # 2 children present
            else:
                current = self.find_min(parent.right)
                parent.value = current.value
                parent.right = self.delete(parent.right, current.value)
        # print(parent.value)
        return parent

    def traverse(self, root):
        if root:
            self.traverse(root.left)
            print(root.value, end = ',')
            self.traverse(root.right)

    def inorder_successor(self, node, val):
        # Search the node with given value, val
        current = self.find(val)
        if current == None:
            return
        else:
            # Case1: presence of right subtree
            if current.right:
                temp = self.find_min(current.right)
                return temp.value
            # Case2: absence of right subtree
            else:
                successor = None
                ancestor = self.root
                while ancestor != current:
                    if current.value < ancestor.value:
                        # Successor is only possible in left subtree
                        successor = ancestor
                        ancestor = ancestor.left
                    else:
                        ancestor = ancestor.right
                if successor:
                    return successor.value
                else:
                    return "None"
    def find_max(self, parent):
        if parent == None:
            return parent
        else:
            current = parent
            while current.right:
                current = current.right
            print("Find Max:{}".format(current.value))
            return current

    def inorder_predecessor(self, val):
        current = self.find(val)
        if current == None:
            return
        else:
            # Case1: presence of left subtree
            if current.left:
                temp = self.find_max(current.left)
                return temp.value
            # Case2: absence of left subtree
            else:
                successor = None
                ancestor = self.root
                while ancestor != current:
                    if current.value > ancestor.value:
                        successor = ancestor
                        ancestor = ancestor.right
                    else:
                        ancestor = ancestor.left
                return successor.value
