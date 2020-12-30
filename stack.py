################ Class ####################
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    

################ Functions ##################

def reverse(word):
    w_Stack = Stack()

    # Class Answer
    for char in word:
        w_Stack.push(char)

    reverse = ""

    while not w_Stack.is_empty():
        reverse = reverse + w_Stack.pop()

    print(reverse)

#TODO: HOMEWORK
#Use a stack to return if a word is a palindrom
#returns True if it is or False if it isn't 
def palindrom(word):
    # Vaiable Instantiation
    reverse = ""   
    reverse_S = Stack()

    #convert string to lower case
    forward = word.lower()

    #split into char array add to Stack
    for char in forward:
        reverse_S.push(char)

    #Fill reverse
    while not reverse_S.is_empty():
        reverse = reverse + reverse_S.pop() 

    ###############
    #Solution 1: Check for palindrom using dunder method
    is_Palindrom = False
    is_Palindrom = reverse.__eq__(forward)

    #return bool
    return is_Palindrom

    ################
    #Solution 2: OR Forced equal check
    # for char in forward:
    #     for char_R in reverse:
    #         if not char == char_R:
    #             return False
    #         return True

#Fn for bracket balance
#fn takes a string of brackets and checks for balance. Returns True or False. 
def balance_check(s):

    #Same as Palindrom???

    #CAN it be a stack? Does it need to be a queue?

    # Vaiable Instantiation
    reverse = ""   
    reverse_S = Stack()

    #split into char array add to Stack
    for char in s:
        reverse_S.push(char)
        print(char)

    #Fill reverse
    while not reverse_S.is_empty():
        reverse = reverse + reverse_S.pop() 
    
    for char in reverse:
        print(char)

    ###############
    #Solution 1: Check for palindrom using dunder method
    # is_Palindrom = False
    # is_Palindrom = reverse.__eq__(s)

    #return bool
    # return is_Palindrom

    ################
    #Solution 2: OR Forced equal check
    for char in s:
        for char_R in reverse:
            if char != char_R:
                return False
            return True

def balance_Check(s):

    #Initial test, return false if not even number of brackets
    if len(s)%2 != 0:
        return False
    
    opening = set('([{')
    matches = set([('(',')'),('[',']'),('{','}')])
    stack = []
    for paren in s:
        print("parent: %s" % paren)
        #add all 'opening brackets'. Continue to balance check when closing brackets are found
        if paren in opening:
            stack.append(paren)
            print("paren i sfound in opening; stack: %s" % stack)
        else:
            if len(stack) == 0:
                print("The stack's length is 0, so this is a failed condition. ")
                return False
            last_open = stack.pop()
            print("Last open (last item from stack): %s" % last_open)

            #test balance of brackets, return false if isn't balanced
            temp_tuple = (last_open, paren)
            if temp_tuple not in matches:
                print("Incorrect tuple match: %s" % str(temp_tuple))
                return False
            else: 
                print("The tuple was found in matches: %s" % str(temp_tuple))
    print("Length of stack: %s" % len(stack))
    return len(stack) == 0

################ Main ####################
if __name__ == "__main__":
    # reverse("Testing")

    # print(palindrom("{[()]}"))

    print(balance_check('{[()]}'))

    print(balance_Check('{[()]}'))
