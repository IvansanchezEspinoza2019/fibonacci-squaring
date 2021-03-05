
""" 
Squaring Algorithm Definition:
    It is used for quickly working out large integer powers 
    of a number.It is also known as the square-and-multiply 
    algorithm or  binary exponentiation. It uses the binary
    expansion of the exponent. It is of quite general use, 
    for example in modular arithmetic. It's complexity is
    log 2 (n).
"""

import numpy as np # numpy module

# initial matrix of fibonacci
F = np.array([[1,1],[1,0]], dtype=object)

def squaringAlgorithm(x, n): # Fibonacci with squaring algorithm

    # receive the initial fibonacci matrix ([1,1], [1,0]) 
    # and the 'n' we want to find. Returns the final cal-
    # culated matrix with the fibonnaci number of 'n'.
   
    if n == 1:
        return x   
    elif n%2 == 0: 
        return squaringAlgorithm(np.dot(x,x), n/2)                  # squaring(x**2, n/2)
    else:           
        return np.dot(x, squaringAlgorithm(np.dot(x,x), (n-1)/2))   # x * squaring(x**2, (n-1)/2)
    

def fibonacci(n):   # Loop Fibonacci
    # loop fibonacci algorithm. in execution time is
    # worse than the squaring algorithm so far. It's
    # complexity is O(n).
    if n == 1:
        return n
    else:
        a, b = 1, 0
        while n>0:
            a, b = b, a+b
            n -= 1
        return b
    

n = int()
try:
    n = int(input("Enter number (int): "))
except ValueError:
    print("Enter only numbers please...")
    quit()

print("\nFibonacci number of "+str(n)+" is: "+str(squaringAlgorithm(F, n)[0,1]))




