#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" FSDI_114 Assignment 3 """

#This assignment creates classes for Stacks and Queues data structures

################ Stack Class ####################
#class that implements a LIFO data association 
class Stack():
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        # return self.items.pop()###

        #alt method without using build-in 'pop' method
        data = self.items[-1]
        self.items.remove(data)
        return data
    
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
    

################ Queue Class ####################
#class that implements a FIFO data association 
class Queue():
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        #one line to return True or False if list is empty
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)



################ Main ####################

if __name__ == "__main__":

    #create Stack object
    new_Stack = Stack()

    new_Stack.push("1")
    new_Stack.push("2")
    new_Stack.push("3")
    new_Stack.push("4")

    #create Queue object
    new_Queue = Queue()

    new_Queue.enqueue("1")
    new_Queue.enqueue("2")
    new_Queue.enqueue("3")
    new_Queue.enqueue("4")

    print("")

    #test Stack methods
    print("Stack Methods: ")
    print("LIFO Pop, Should be 4: " + str(new_Stack.pop()))
    print("Is Stack empty: " + str(new_Stack.is_empty()))
    print("Length Should equal 3: " + str(new_Stack.size()))
    print("I'm peeking and should be 3: " + str(new_Stack.peek()))

    print("*" * 40)
    print("*" * 40)
    print("")

    #test Queue methods
    print("Queue Methods: ")
    print("FIFO dequeue, Should be 1: " + str(new_Queue.dequeue()))
    print("Is Queue empty: " + str(new_Queue.is_empty()))
    print("Length should be 3: " + str(new_Queue.size()))

