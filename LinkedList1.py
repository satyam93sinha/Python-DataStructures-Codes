class Element:
    """Individual Linked Lists

    declares an element with value and address to next linked list element.
    Here, next will be none"""

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """Implementation

    Implementing linked list"""
    def __init__(self, head = None):
        self.head = head
        self.linked_list = {}

    def append(self, new_element):
        current = self.head
        if self.head:
            print(current.value)
            while current.next:
                # print(current.value)
                current = current.next
                print(current.value)
            current.next = new_element
        else:
            self.head = new_element

    def view(self):
        current = self.head
        i = 1
        if self.head:
            self.linked_list[i] = current.value
            print(current.value)
            while current.next:
                current = current.next
                i += 1
                self.linked_list[i] = current.value
                print(self.linked_list)

        else:
            print("No head, empty linked list")

    def get_position(self, position):
        self.view()
        linked_list_keys = self.linked_list.keys()
        print(linked_list_keys)
        if position in linked_list_keys:
            print(self.linked_list[position])
        else:
            print("None")

    
        
                
                
    
