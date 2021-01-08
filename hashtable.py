
#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Algorithm Solution: Anagrams"""



class HashTable(object):
    def __init__(self, size):
        #set up size and slots and data
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
    def put(self, key, data):
        #Note, we'll only use integer keys for ease of use with the Hash Function
        #get the hash value
        hashvalue = self.hashfunction(key, len(self.slots))

        # If slot is Empty
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            #If key already exists, replace old value
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            #Othersie, find the next available slot
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                # Get to the next slot
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                    #Set new key, if NONE
                    if self.slots[nextslot] == None:
                        self.slots[nextslot] = key
                        self.data[nextslot] = data
                    #Otherise replace old value 
                    else:
                        self.data[nextslot] = data
    
    def hashfunction(self, key, size):
        return key%size


    def rehash(self, oldhash,size):
        return (oldhash+1)%size
    
    def get(self, key):
        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key, data)


#Fibonacci sequence. Sum of previous two numbers. 
#Big O notation is O(N)
def fib(n, hashtable):
    #Calculate the key
    key = hashtable.hashfunction(n, hashtable.size)

    #Base case: check if value exists in hash table
    value = hashtable.get(key) 

    if value:
        return value

    #First two numbers in Fib seq
    if n < 2:
        #put in hash table
        hashtable.put(key,n)

        return n

    #Calculate Fib number
    data = fib(n-1, hashtable) + fib(n-2, hashtable)
    #store value
    hashtable.put(key, data)

    return data


if __name__ == "__main__":

    
    #calculate fibonacci from 1 to 100, sequentially 
    #Fibonacci sequence. Sum of previous two numbers. 

    #create hash table
    fib_Hash = HashTable(100)

    
    #calculate each number and print the numbers in Fib sequence 
    for i in range(1, 100):
        value = fib(i, fib_Hash)
        print(value)


