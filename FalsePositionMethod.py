import numpy as np
import matplotlib.pyplot as plt
import math

class state:
    def __init__(self, x_n, x_p, x_m, err, f_xm):
        self.x_n = x_n
        self.x_p = x_p
        self.x_m = x_m
        self.err = err
        self.f_xm = f_xm


class FalsePosition:
     def __init__(self, x1, x2):
        if FalsePosition.function(x1)<0 < FalsePosition.function(x2):
            self.x_neg = x1
            self.x_pos = x2
        elif FalsePosition.function(x2)<0 < FalsePosition.function(x1):
            self.x_neg = x2
            self.x_pos = x1
        else:
            raise ValueError('Invalid Initial Value')
        self.x_mid = None


     @staticmethod
     def function(x):
        return x*math.tan(x)-3
        return -13-20*x+19*x*x-3*x*x*x

     @staticmethod
     def error(x_new, x_old):
        if x_old is None:
            return None
        return 100*(x_new-x_old)/x_new

     @staticmethod
     def get_mid(x1,x2):
        return ((-FalsePosition.function(x1)*(x1-x2))/(FalsePosition.function(x1)-FalsePosition.function(x2)))+x1

     def run(self):
        new_mid = FalsePosition.get_mid(self.x_pos,self.x_neg)
        error = FalsePosition.error(new_mid, self.x_mid)
        self.x_mid = new_mid
        f_x = FalsePosition.function(self.x_mid)
        st = state(self.x_neg,self.x_pos,self.x_mid,error,f_x)
        if f_x > 0:
            self.x_pos = self.x_mid
        else:
            self.x_neg = self.x_mid
        return st


fp = FalsePosition(float(input('Enter x1: ')), float(input('Enter x2: ')))
iterations = int(input('Enter Iterations: '))
xm, err, fxm = [], [], []

for i in range(iterations):
    st = fp.run()
    print(i+1, st.x_n, st.x_p, st.x_m, st.err, st.f_xm)
    xm.append(st.x_m)
    err.append(st.err)
    fxm.append(st.f_xm)
    '''
plt.plot(xm)
plt.ylabel('X mid')
plt.xlabel('Iterations')
plt.show()
plt.ylabel('Error')
plt.xlabel('Iterations')
plt.plot(err)
plt.show()
plt.ylabel('F(X mid)')
plt.xlabel('X mid')
plt.scatter(xm,fxm)
plt.show()'''