#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Algorithmic Solution Funtions """

import os
import subprocess

#1) Fn that take an input string and returns
#   the reverse, using a char recursive fn
def reverse(word):
    # variable declaration
    backwards = ""
    shortened = []

    #Base Case: When input string is empty, return output string
    if len(word) == 0:

        return backwards

    #Recursive fn
    else:
        #create char array
        for w in word:
            shortened.append(w)
        
        # Add to backwards string, remove ea. char from array
        while(shortened):
            backwards += str(shortened.pop())
            
        #recursive fn call until empty string is passed
        backwards += reverse(shortened)
        
    #print output string to console
    return backwards

#2) Fn that takes an input list of integers
#   and returns a list of product results, minus 
#   one list element
def product_Replacement(int_List):

    #grab length of input list
    length = len(int_List)

    #variable declaraton
    productArray = []
    x = 0
    sum = 1

    #repeat for every element in input array
    while(length != 0):
        for item in int_List:
            #multiply and add to sum if not current index
            if(int_List.index(item) != x):
                sum = sum * item 
        
        #add sum to output list
        productArray.insert(x, sum)

        #deincrement and increment counters
        length = length - 1 
        x = x+1
        sum = 1


    #print output string to console
    print('*******************************')
    print(' Multiplication Results:       ')
    print('*******************************')

    print('Original Integer Values: ')
    for i in int_List:
        print('        ' + str(i) + '        ')
    
    print('Resulant Product Values: ')
    for p in productArray:
        print('        ' + str(p) + '        ')
    print('-' * 20)


# Function to run program until 'exit'
def main_View():
    clear()
    print_menu()
    # Get User Input
    opc = input("Please select an option: ")

    while(opc != 'x'):
        # Execute correct user choice
        if(opc == '1'):
            ux_word = ""
            ux_word = str(input("Enter a word would you like printed backwards: "))
            result = reverse(str(ux_word))

            #print to console
            print('*******************************')
            print(' Word Reverse Result:          ')
            print('*******************************')

            print(str(result))
            print('-' * 20) 

            # Wait for user to see answer, then choose to continue or exit
            answer = input("Would you like to choose the main again? Y/N:  ")
            if(answer == 'Y' or answer == 'y'):
                clear()
                main_View()
            else:
                clear()
                break

        elif(opc == '2'):
            length = int(input("Enter number of integers to be multiplied: "))

            i = 0
            simpleList = []

            while(length != 0):
                x = int(input("Enter number " + str(i+1) + ": "))
                simpleList.insert(i, x)
                i = i + 1
                length = int(length - 1)

            product_Replacement(simpleList)
            
            # Wait for user to see answer, then choose to continue or exit
            answer = input("Would you like to choose the main again? Y/N:  ")
            if(answer == 'Y' or answer == 'y'):
                clear()
                main_View()
            else:
                clear()
                break


    print("~Thank You! Good byte!~")
    clear()
    # return True

# Function to clear console
def clear():
    if os.name in ('nt', 'dos'):
        subprocess.call("cls")
    elif os.name in ('linux', 'osx', 'posix'):
        subprocess.call("clear")

def print_menu():
    print('*******************************')
    print(' Welcome - Algorithm Solutions ')
    print('*******************************')

    print('[1] Reverse a Word')
    print('[2] Multiplication Challenge')

    print('[x] Exit')
    print('-' * 20)  


if __name__ == "__main__":

    opc = ""

    main_View()
    