import math
import matplotlib.pyplot as plt

def J(n,x):
    ans= pow(x/2,n)
    temp=0
    for k in range (1,96):
        a=pow(-1,k)
        b=pow((pow(x,2)/4),k)
        c=math.factorial(k)*math.factorial(n+k)
        temp+=a*b/c;
    return ans*temp


x0=[]
x1=[]
x2=[]

x=0.0
while x<=10.0:
    x0.append(J(0,x))
    x1.append(J(1,x))
    x2.append(J(2,x))
    x+=0.1

plt.plot(x0)
plt.show()
plt.plot(x1)
plt.show()
plt.plot(x2)
plt.show()

