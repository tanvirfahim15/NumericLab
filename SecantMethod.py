def funct(x):
    return pow(x, 3) - 0.165 * pow(x, 2) + 3.993 * pow(10, -4)

def new(x_i,x_i_1):
    return x_i-funct(x_i)*(x_i-x_i_1)/(funct(x_i)-funct(x_i_1))

x_i=0.02
x_i_1=0.05

for i in range(6):
    n=new(x_i,x_i_1)
    print(n)
    print(funct(n))
    print()
    x_i=x_i_1
    x_i_1=n