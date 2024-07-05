# Fixed Point Iteration Method
# Importing math to use sqrt function
import math

def f(x):
    return x*x*x + x*x -1

def g(x):
    return 1/math.sqrt(1+x)

def fixedPointIteration(x0, e,):
    
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1

        step = step + 1
        
        condition = abs(f(x1)) > e

    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

x0 = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))


fixedPointIteration(x0,e)