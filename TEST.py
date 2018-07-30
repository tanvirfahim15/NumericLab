def function(x):
    return pow(x-1, 3) +0.512
def func(x):
    return 3*pow(x-1, 2)
def newx(x):
    return x-function(x)/func(x)

xold=0
x=5


for i in range(7):
    print('fx: '+str(function(x)))
    print('dx: '+str(func(x)))
    print('x(i+1): '+str(newx(x)))
    print('error: '+str((x - xold) / x))
    xold=x
    x=newx(x)
    print()
    print()