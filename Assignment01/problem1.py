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
            raise ValueError('No root possible')
        self.x_mid = None

    @staticmethod
    def function(m):
        g = 9.8
        c = 15.0
        v = 35.0
        t = 9.0
        try:
            result = (g*m/c)*(1-math.exp(-c*t/m)) - v
            return result
        except ZeroDivisionError:
            raise ValueError('Function not continuous on '+ str(m))

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


class FalsePosition:
    def __init__(self, x1, x2):
        if FalsePosition.function(x1) < 0 < FalsePosition.function(x2):
            self.x_neg = x1
            self.x_pos = x2
        elif FalsePosition.function(x2) < 0 < FalsePosition.function(x1):
            self.x_neg = x2
            self.x_pos = x1
        else:
            raise ValueError('Invalid Initial Value')
        self.x_mid = None

    @staticmethod
    def function(m):
        g = 9.8
        c = 15.0
        v = 35.0
        t = 9.0
        try:
            result = (g * m / c) * (1 - math.exp(-c * t / m)) - v
            return result
        except ZeroDivisionError:
            raise ValueError('Function not continuous on ' + str(m))

    @staticmethod
    def error(x_new, x_old):
        if x_old is None:
            return None
        return 100 * (x_new - x_old) / x_new

    @staticmethod
    def get_mid(x1, x2):
        return ((-FalsePosition.function(x1) * (x1 - x2)) / (
                    FalsePosition.function(x1) - FalsePosition.function(x2))) + x1

    def run(self):
        new_mid = FalsePosition.get_mid(self.x_pos, self.x_neg)
        error = FalsePosition.error(new_mid, self.x_mid)
        self.x_mid = new_mid
        f_x = FalsePosition.function(self.x_mid)
        st = state(self.x_neg, self.x_pos, self.x_mid, error, f_x)
        if f_x > 0:
            self.x_pos = self.x_mid
        else:
            self.x_neg = self.x_mid
        return st


def frange(start, stop, step):
    result = [start]
    while start <= stop:
        start += step
        result.append(start)
    return result


x1 = float(input('Enter x1: '))
x2 = float(input('Enter x2: '))
for m in frange(x1, x2, 0.1):
    print(m, Bisection.function(m))


bs = Bisection(x1, x2)

xm_bs, err_bs, fxm_bs = [], [], []

tolerance = pow(10, -int(input('Enter tolerance: ')))

print('Bisection Method: ')
i = 0
while True:
    st = bs.run()
    print(i+1, st.x_n, st.x_p, st.x_m, st.f_xm, st.err)
    i = i + 1
    xm_bs.append(st.x_m)
    err_bs.append(st.err)
    fxm_bs.append(st.f_xm)
    if st.err is not None and tolerance > st.err > -tolerance:
        break


fp = FalsePosition(x1, x2)

xm_fp, err_fp, fxm_fp = [], [], []

print('False Position Method: ')
i = 0
while True:
    st = fp.run()
    print(i+1, st.x_n, st.x_p, st.x_m, st.f_xm, st.err)
    i = i + 1
    xm_fp.append(st.x_m)
    err_fp.append(st.err)
    fxm_fp.append(st.f_xm)
    if st.err is not None and tolerance > st.err > -tolerance:
        break

plt.scatter(xm_bs, err_bs)
plt.xlabel('x')
plt.ylabel('Error')
plt.show()

plt.ylabel('Error')
plt.xlabel('Iterations')
plt.plot(err_bs)
plt.show()

plt.scatter(xm_fp, err_fp)
plt.xlabel('x')
plt.ylabel('Error')
plt.show()

plt.ylabel('Error')
plt.xlabel('Iterations')
plt.plot(err_fp)
plt.show()


plt.ylabel('Error')
plt.xlabel('Iterations')
plt.plot(err_bs)
plt.plot(err_fp)
plt.show()

plt.ylabel('Error')
plt.xlabel('Iterations')
plt.scatter(xm_bs, err_bs)
plt.scatter(xm_fp, err_fp)
plt.show()


