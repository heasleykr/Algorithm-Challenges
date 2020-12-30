#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Algorithm Solution: Anagrams"""


#1) Function that checks if two strings are anagrams of eachother
#   Returns boolean value
def anagram(word_1, word_2):
    
    #Variable declaration
    charArray = []
    charArray2 = []

    #store both strings in char array
    for char in word_1:
        charArray.append(char)
    
    for char in word_2:
        charArray2.append(char)

    #basse case: Check length of both arrays
    if len(charArray) != len(charArray2):
        result(0)
        return False
    
    else:
        #loop through string 1, locate char in string 2
        for char in word_1:
            x = word_2.find(char)
            #if char isn't found, stop search
            if x == -1:
                result(x)
                return False
        
        #Verify & repeat backwards: Lopp through string 2, locate char in string 1
        for char in word_2:
            x = word_1.find(char)
            #if char isn't found, stop search
            if x == -1:
                result(x)
                return False

        #return True if -1 wasn't returned. 
        result(1)
        return True

#function to display output separator
def print_Pretty():
    print("")
    print('*' * 70) 
    print('-' * 70)
    print("") 

#function to display result message to screen
def result(r):
    #False return value for length 
    if r == 0:
        print_Pretty()
        print("False: The strings do not have the same number of characters, therefore they are not anagrams!")
        print_Pretty()
    #False return value for character search
    elif r == -1:
        print_Pretty()
        print("False: The strings do not include the same letters, therefore they are not anagrams!")
        print_Pretty()
    #True return value
    elif r == 1:
        print_Pretty()
        print("True: The words are anagrams of each other!")
        print_Pretty()

#function to grab user input

if __name__ == "__main__":

    #grab user input
    print_Pretty()
    print("Welcome! Let's choose two words and discover if they're anagrams!")
    print_Pretty()
    first = input("Enter the first word: ")
    second = input("Enter the second word: ")


    is_Anagram = anagram(first, second)

    print(is_Anagram)
