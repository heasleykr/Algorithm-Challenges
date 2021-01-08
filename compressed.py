#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Compressed Challenge """

#Algo challenge solution to take a string, collapse the recurring chars and return a compressed version 
# Worst Case RT is O(2n) => or O(n)
def compress(word):

    #var declaration
    char_List = []
    i = 0
    counter = 0
    dup_Char = ""
    compressed = ""

    #Make a list 
    #O(n)
    for char in word:
        char_List.append(char)
    
    #grab first char, add char to compressed string
    dup_Char = char_List[i]
    compressed += dup_Char

    #continue char evaluation until end of char list
    #O(n)
    while(i < len(char_List)):
        #While sequential chars match AND end of list is not reached, add to counter, increment index
        while(i < len(char_List) and char_List[i] == dup_Char):
            counter += 1
            i += 1
        
        #Add counter value to compressed string, reset counter
        compressed += str(counter)
        counter = 0

        #Reset: If not at end - Update new char & add to compressed string
        if i < len(char_List):
            dup_Char = char_List[i]
            compressed += dup_Char
    
        
    #Finally: Compare length of orginial and compressed string, return shortest
    if len(word) < len(compressed):
        print("Your string is already at it's shortest length: compression not needed. ")
        return word 

    print("Your compressed String: ")    
    return compressed 

################# Main ###########################

if __name__ == "__main__":

    #Trial to return compressed string
    print(compress("aaabbbccc"))

    #Trial to return original string
    print(compress("abcde"))