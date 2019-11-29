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
