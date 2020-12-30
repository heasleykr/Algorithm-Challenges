#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" A Simple LinkedList Class """

# class for linked list #

def LinkedList():
    def __init__(self):
        self.head = None
    
    #method to add to beginning of list
    def push(self, newHead):
        #link to head Node
        newHead.next = self.head

        #assign head value to new node
        self.head = newHead
    
    #method to add to end of list 
    #TODO: add edge cases of empty list 
    def append(self, newTail):
        #grab first element
        tail = self.head 

        #traverse through the list until you have tail
        while(tail):
            tail = tail.next
        
        #link new node to end
        tail.next = newTail

        #Add 'Null' to end??
        newTail.next = None

    #TODO: find a node given it's data. 
    def findNode():
        

    def insertAfter(self, currentNode, newNode):

        #grab current 'next' 
        nextNode = currentNode.next

        #insert node
        currentNode.next = newNode

        #assign value after
        newNode.next = nextNode

    def remove(self, deleteNode):
        #start at head. Also grad pointer to be linked
        previous = self.head
        nextNode = deleteNode.next

        #find the node that is previous to deletion
        while previous:
            if previous.next = deleteNode:
                break
        
        #assign next link
        previous.next = nextNode
                
        

    
    def print_list(self):
        #grab first element
        nodeIndex = self.head

        #print data while the tail isn't reached
        while nodeIndex:
            print(nodeIndex.data)
            nodeIndex = nodeIndex.next


if __name__ == "__main__"
    
