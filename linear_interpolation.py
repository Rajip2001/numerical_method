

print('Enter first point:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Enter second point:') 
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))


xp = float(input('Enter calculation point xp: '))

yp = y0 + ((y1-y0)/(x1-x0)) * (xp - x0)


print('Interpolated value at %0.4f is %0.4f' %(xp,yp))