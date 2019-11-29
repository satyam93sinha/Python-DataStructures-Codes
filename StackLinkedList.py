class Node:
    def __init__(self, node):
        self.value = node
        self.next = None

class StackLinkedList:
    def __init__(self, head=None):
        self.head = head

    def isEmpty(self):
        if self.head:
            return False
        else:
            return True

    def push(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def pop(self):
        temp = self.head
        del self.head
        self.head = temp.next
        return temp.value

    def peek(self):
        return self.head.value

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def reverse_linked_list(self):
        # time complexity: O(n)
        # space complexity: O(n)
        current = self.head
        list_ = []
        while current.next:
            list_.append(current)
            current = current.next
        print(list_)
        self.head = current
        while len(list_):
            current.next = list_.pop()
            current = current.next
        current.next = None

    def balanced_parenthesis(self, exp):
        stack = []
        count = 0
        for i in exp:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            elif i==')' or i=='}' or i==']':
                if (stack[len(stack)-1]=='(' and i==')') or (stack[len(stack)-1]=='{' and i=='}') or (stack[len(stack)-1]=='[' and i==']'):
                    stack.pop()
                    count += 1
                else:
                    return ("Unbalanced", stack)
        print(stack, count)
                

            
