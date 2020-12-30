from stack import Stack


################### Classes #############

# class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self):
        self.items.insert(0,items)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

# IMPLEMENT A QUEUE USING TWO STACKS
class Queue2Stacks:
    def __init__(self):
        self.stackAdd = []
        self.stackRemove = []
    
    #add to stackAdd. Will be in reverser order
    def enqueue(self, element):
        #add to first stack
        self.stackAdd.append(element)

    #on print, add everything to stackRemove, then pop
    def dequeue(self):
        if not self.stackRemove:
            while self.stackAdd:
                self.stackRemove.append(self.stackAdd.pop())
        return self.stackRemove.pop()


############# Functions ##############

def test():
    # this should print: 0,1,2,3,4
    # Note: It will print vertically
    q = Queue2Stacks()
    for i in range(5):
        q.enqueue(i)
    for i in range(5):
        print(q.dequeue())


############ Main ###################

if __name__ == "__main__":
    test()
