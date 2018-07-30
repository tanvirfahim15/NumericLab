import numpy as np
import matplotlib.pyplot as plt
class state:
    def __init__(self, x_n, x_p, x_m, err, f_xm):
        self.x_n = x_n
        self.x_p = x_p
        self.x_m = x_m
        self.err = err
        self.f_xm = f_xm

class Bisection:
     def __init__(self, x1, x2):
        if Bisection.function(x1)<0 < Bisection.function(x2):
            self.x_neg = x1
            self.x_pos = x2
        elif Bisection.function(x2)<0 < Bisection.function(x1):
            self.x_neg = x2
            self.x_pos = x1
        else:
            raise ValueError('Invalid Initial Value')
        self.x_mid = None

     @staticmethod
     def function(x):
        return pow(x, 3)-0.165*pow(x, 2)+3.993*pow(10, -4)

     @staticmethod
     def error(x_new, x_old):
        if x_old is None:
            return None
        return 100*(x_new-x_old)/x_new

     def run(self):
        new_mid = (self.x_neg + self.x_pos) / 2
        error = Bisection.error(new_mid, self.x_mid)
        self.x_mid = new_mid
        f_x = Bisection.function(self.x_mid)
        st = state(self.x_neg,self.x_pos,self.x_mid,error,f_x)
        if f_x > 0:
            self.x_pos = self.x_mid
        else:
            self.x_neg = self.x_mid
        return st


bs = Bisection(float(input('Enter x1: ')), float(input('Enter x2: ')))
iterations = int(input('Enter Iterations: '))
xm, err, fxm = [], [], []
for i in range(iterations):
    st = bs.run()
    print(i+1, st.x_n, st.x_p, st.x_m, st.err, st.f_xm)
    xm.append(st.x_m)
    err.append(st.err)
    fxm.append(st.f_xm)
plt.plot(xm)
plt.ylabel('X mid')
plt.xlabel('Iterations')
plt.show()
plt.ylabel('Error')
plt.xlabel('Iterations')
plt.plot(err)
plt.show()
plt.ylabel('F(X mid)')
plt.xlabel('Iterations')
plt.plot(fxm)
plt.show()