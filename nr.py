def f(x):
    return x**3 - 5*x - 9

def g(x):
    return 3*x**2 - 5

def newtonRaphson(x0, e):
    step = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 - f(x0) / g(x0)
        print(f'Iteration-{step}, x1 = {x1:0.4f} and f(x1) = {f(x1):0.4f}')
        x0 = x1
        step += 1

        condition = abs(f(x1)) > e
    
    print('\nRequired root is: %0.4f' % x1)

x0 = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))
newtonRaphson(x0, e)
