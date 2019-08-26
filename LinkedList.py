class Element:
    def __init__(self, elem):
        self.element = elem
        # self.current = None
        self.next = None
        print(self.element, self.next)

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        # print(self.head)

    def append_linked(self, value):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
                # print(current)
            current.next = value
            # print(current.next)
        else:
            self.head = value
    def linked_list_view(self):
        current = self.head
        count = 0
        if self.head:
            print("if:{}".format(current.element))
            while current:
                print("while:{}".format(current.element))
                current = current.next
                

    def delete_first(self):
        if self.head:
            self.head = self.head.next
        else:
            self.head = None

    def insert_first(self, new_element):
        if self.head:
            self.head, new_element.next = new_element, self.head
        else:
            self.head = new_element

                    
                

