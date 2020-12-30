def sum_iterative(n):
    #how many times does this go? N times
    #range starts at zero  so 'n+1'
    out = 0
    for i in range(n+1):
        out += i
    return out

#Recursion
#if you give value of 10, it's going to loop backwards. Generates a stack in memory
#Consumes a lot of memory
#Python has a maximum recursive depth. Memo-ization 
def sum_recursive(n):
    #base case
    if n == 1:
        return 1
    
    return n+sum_recursive(n-1)

#This is the best solution to solve the problem. There are no loops, no recursion. And it's not linear.
def sum_optimal(n):
    return (n*(n+1))/2
