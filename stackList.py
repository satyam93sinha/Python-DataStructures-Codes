import numbers
class Stack:
    """Stack-Data Structure

    Last-In-First-Out Abstract Data Structure, built on the basis of different
    data structures as List, Arrays, LinkedList etc.
    Four Operations:
    1. Push() - adds/appends an element to the stack.
    2. Pop() - removes and displays the recently added element from the stack.
    3. Peek()/Top() - returns the top element of the stack.
    4. isEmpty() - checks if the stack is empty. """

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


    def push(self, element):
        self.stack.append(element)
        print(self.stack)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            print(self.stack[len(self.stack)-1:])
            del self.stack[len(self.stack)-1:]

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            print(self.stack[len(self.stack)-1:])

    def balanced_parentheses(self, parentheses):
        self.parentheses = parentheses
        count = 0
        for i in parentheses:
            if i == '(' or i == '{' or i == '[':
                self.stack.append(i)
            elif i == ')':
                if self.stack[len(self.stack)-1] == '(':
                    self.pop()
                    count += 1
            elif i == '}':
                if self.stack[len(self.stack)-1] == '{':
                    self.pop()
                    count += 1
            elif i == ']':
                if self.stack[len(self.stack)-1] == '[':
                    self.pop()
                    count += 1
            else:
                continue
                #return "Only Parentheses not found, Invalid Input"
        print("Count of parentheses: {}".format(count))

    def postfix_evaluation(self, exp):
        self.exp = exp.split(' ')
        for i in self.exp:
            try:
                if isinstance(int(i), numbers.Number):
                    self.stack.append(int(i))
                    print("self.stack: {}".format(self.stack))
            except ValueError:
                if i == '+':
                    self.stack[len(self.stack)-2] = self.stack[len(self.stack)-2] + self.stack[len(self.stack)-1]
                    self.pop()
                elif i == '-':
                    self.stack[len(self.stack)-2] = self.stack[len(self.stack)-2] - self.stack[len(self.stack)-1]
                    self.pop()
                elif i == '*':
                    self.stack[len(self.stack)-2] = self.stack[len(self.stack)-2] * self.stack[len(self.stack)-1]
                    self.pop()
                elif i == "/":
                    self.stack[len(self.stack)-2] = self.stack[len(self.stack)-2] / self.stack[len(self.stack)-1]
                    self.pop()
        print(self.stack)

        """def infix_to_postfix(self, exp):
            self.exp = exp.split(' ')"""
            
            
                    
