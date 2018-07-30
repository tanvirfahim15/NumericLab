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


class Bisection:

    def __init__(self, x1, x2):
        if Bisection.function(x1)<0 < Bisection.function(x2):
            self.x_neg = x1
            self.x_pos = x2
        elif Bisection.function(x2)<0 < Bisection.function(x1):
            self.x_neg = x2
            self.x_pos = x1
        else:
            self.x_neg = x2
            self.x_pos = x1
            '''raise ValueError('Solution Impossible')'''
        self.x_mid = None

    @staticmethod
    def function(x):
        n=0
        ans = 1
        temp = 0.0
        for k in range(1, 11):
            a = pow(-1, k)
            b = pow((pow(x, 2) / 4), k)
            c = math.factorial(k) * math.factorial(k)
            temp += a * b / c;
        return ans * temp

    @staticmethod
    def error(x_new, x_old):
        if x_old is None:
            return None
        return math.fabs((x_new-x_old)/x_new)

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


x=1
while x<3.1:
    print(x)
    print(Bisection.function(x))
    print()
    x+=0.1

tolerance_flag = False
if input()=='1':
    tolerance_flag = True

bs = Bisection(float(input('Enter x1: ')), float(input('Enter x2: ')))

xm, err, fxm = [], [], []

if tolerance_flag is False:
    iterations = int(input('Enter Iterations: '))
    for i in range(iterations):
        st = bs.run()
        print(i + 1, st.x_n, st.x_p, st.x_m, st.err, st.f_xm)
        xm.append(st.x_m)
        err.append(st.err)
        fxm.append(st.f_xm)
else:
    tolerance = pow(10, -int(input('Enter Tolerance:')))
    temp_tolerance = None
    i = 0
    while temp_tolerance is None or temp_tolerance>tolerance:
        st = bs.run()
        print(i + 1, st.x_n, st.x_p, st.x_m, st.err, st.f_xm)
        xm.append(st.x_m)
        err.append(st.err)
        fxm.append(st.f_xm)
        temp_tolerance=st.err
        i += 1


'''
plt.plot(xm)
plt.ylabel('X mid')
plt.xlabel('Iterations')
plt.show()
'''
plt.ylabel('Error')
plt.xlabel('xm')
plt.plot(xm,err)
plt.show()
plt.clf()
plt.ylabel('it')
plt.xlabel('err')
'''
ax1 = plt.subplot()

ax1.set_ylim(-.0005,.0005)
ax1.set_xlim(0.05,.09)
'''
plt.plot(err)
plt.show()