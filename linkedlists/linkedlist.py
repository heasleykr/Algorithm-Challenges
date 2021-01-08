#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" A Simple LinkedList Class """

# from node.py import Node

############ Node Class ###################
def Node:
    def __init__(self, data):
        self.next = None 
        self.data = data

    def get_data(self):
        return self.data
    
    def __str__(self):
        return self.get_data()

################## Class for LinkedList ###################

def LinkedList:
    def __init__(self):
        self.head = None
    
    #method to add to beginning of list
    def push(self, newHead):

        #check if list has head, make head if None 
        if self.head == None:
            self.head = newHead
        
        #reassign new head to list and make the head the tail. 
        else:
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

        #Add 'Null' to end
        newTail.next = None

    #Medthod to find a node given it's data. 
    def findNode(self, node_Data):

        #start at the beginning of the list
        search = self.head

        #traverse through the list while you haven't gotten to tail.
        while(search):
            if(search.data == node_Data):
                #return Node if data maches query
                return search
            
        #else return node-not-found
        return None

        
    #method to add node to center of list after a given node passed as a parameter
    def insertAfter(self, currentNode, newNode):

        #grab current 'next' 
        nextNode = currentNode.next

        #insert node
        currentNode.next = newNode

        #assign value after
        newNode.next = nextNode
    

    #method to remove Node given the object as a parameter
    def remove(self, deleteNode):
        #start at head. Also grab pointer to be linked
        previous = self.head
        nextNode = deleteNode.next

        #find the node that is previous to deletion
        while previous:
            if previous.next == deleteNode:
                break
        
        #assign next link
        previous.next = nextNode
                
############### Functions ##################

def print_list():
    #grab first element
    nodeIndex = self.head

    #print data while the tail isn't reached
    while nodeIndex:
        print(nodeIndex.data)
        nodeIndex = nodeIndex.next


################ Main ####################

if __name__ == "__main__":

    #initial List object
    list = LinkedList()

    #initiate Node to place into list
    n1 = Node('Node 1')
    n2 = Node('Node 2')
    n3 = Node('Node 3')

    #loop and add to list, link them
    list.push(n1)
    list.push(n2)
    list.push(n3)
    
    list.print_list()
    #print tests to evalulate all methods on the list class. 
