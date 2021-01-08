#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Algorithm Challenges """

from linkedlists/linkedlist.py import LinkedList 
from linkedlists/node.py import Node

#implement an algorithm to determine if string has all unique characters
def unique(word):

    #make string lower
    lowercase = word.lower()

    #make list
    seen = []
    #loop through the string and add to list 
    for char in lowercase:
        #if the char is already in list, return false
        if char in seen:
            return False
        
        seen.append(char)
    
    return True


#Challenge: Implement a function to check if a linked list is a palindrome
#Q: Does the solution have to consider a single linked list or double linked list? Doubly linked-list
def palindrom(list):

    #Base Case 1: If List is empty, return False
    if len(list) == 0:
        return False
    #Base Case 2: If List contains one value, return True
    if len(list) == 1:
        return True
    #Base Case 3: compare tail / head
    if list.head != list.tail:
        return False
    
    #Delare check variables 
    forward = list.head.nextNode
    backward = list.tail.previousNode
    
    #iterate through list, compare, return false at any point
    #if they arrive on same node, stop loop
    while(forward.nextNode != backward.nextNode):
        if forward.data != backward.data:
            return False
      
    return True


#Algorithm challenge 3
#Implementcompressed string email Professor 


#write a fn to recursively print numbers from 0 to n
def print_Expand(n):

    print(n)

    if n == 0:
        return n
    
    return recursive_count(n-1)
        



if __name__ == "__main__":
    
    word_list = ["abccc", "abcde", "abbcde"]

    for w in word_list:
        print("%s is unique? -> %s" % (w, unique(w)))

