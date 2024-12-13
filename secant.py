def f(x):
    return x**3 - 5*x - 9



def secant(x0,x1,e):
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break
        
        x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1
        
        condition = abs(f(x2)) > e
    print('\n Required root is: %0.8f' % x2)

x0 = float(input('Enter First Guess= '))
x1 = float(input('Enter Second Guess= '))
e = float(input('Tolerable Error= '))

secant(x0,x1,e)
