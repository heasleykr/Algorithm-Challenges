# Factorials using recursion
def fact(n):
    # base. If n=0, then n! = 1
    if n == 0:
        return 1
    # else, calculate all the way until through
    return n*fact(n-1)

    # one liner
    # return 1 if not n else n*fact(n-1)


def fact_loop(n):
    # base case return n if  0
    # if n == 0:
    #     return n
    # else:
        sum_ = n
    # else, calculate all the way until through
        while n != 1:
            n = n-1
            sum_ *= n
        return sum_

#Fibonacci sequence. Sum of previous two numbers. 
def fib(n):
    #base case
    if n < 2:
        return n

    #Calculate Fn 
    return fib(n-1) + fib(n-2)
    
#homework TODO: How to cut this in half? store previous calculations
#homework TODO: Turn fibonaci into iterative fn. 


if __name__ == '__main__':
    # print(fact(6))

    print(fact_loop(6))
