# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 18:08:47 2019

@author: Sinha
"""

class Node:
    # Constructor to create a Node
    def __init__(self, node):
        self.value = node
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
        self.linked_list = {}
    
    # Insert/append to Linked List
    def insert(self, element):
        # Node(elem)- can't have, bcoz it doesn't make elem
        # an object of Node/node but elem stays int/same data type as passed.
        if self.head == None:
            self.head = element
            # print("Head:{}".format(self.head.value))
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = element
            # print(current.next.value)
     
    # Traverse a Linked List
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    # Determine len of Linked List
    def len_linked_list(self):
        self.count = 0
        current = self.head
        while current:
            self.linked_list[self.count] = current.value
            current = current.next
            self.count += 1
        return self.count
    
    # Insert node at nth position
    def nth_insert(self, elem, n):
        len_ = self.len_linked_list()
        if n == 0:
            self.head = elem
        elif n <= len_:
            current = self.head
            for i in range(0, n-1):
                current = current.next
            elem.next = current.next
            current.next = elem
        else:
            return "Invalid n"
        
    # Delete node from nth position
    def nth_delete(self, n):
        if n == 0:
            self.head = self.head.next
        elif n <= self.count:
            current = self.head
            for i in range(0, n-1):
                current = current.next
            current.next = current.next.next
            return self.len_linked_list()
        else:
            return "Invalid position"
        
    # Reverse Linked List - Iterative Method
    def reverse_iteration(self):
        prev = None
        current = self.head
        temp = self.head
        while current:
            temp = temp.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
        return self.traverse()
    
    # Delete Linked List completely freeing memory
    def delete_list(self):
        prev, current = self.head, self.head
        while current:
            prev = current.next
            del current.value
            current = prev
        print("Linked List Deleted")
        
    def recursion_traversal(self, node):
        if node:
            print(node.value)
            self.recursion_traversal(node.next)
        return
    
    def reverse_recursion_traversal(self, node):
        if node:
            self.reverse_recursion_traversal(node.next)
            print(node.value)
        return
    
        