import math
import matplotlib.pyplot as plt


class Status:
    def __init__(self, i, x, fx, dfx, err):
        self.i = i
        self.x = x
        self.fx = fx
        self.dfx = dfx
        self.err = err

    def print(self):
        print(self.i, self.x, self.fx, self.dfx, self.err)


class NewtonRaphson:

    def __init__(self, x0):
        self.x0 = x0

    def f(self, x):
        pass

    def df(self, x):
        pass

    @staticmethod
    def error(x_old, x_new):
        if x_old is None or x_new is None:
            return None
        return math.fabs((x_new-x_old)/x_new)

    def run(self, iterations=None,tolerance=None):
        status_s = []
        x_im1 = None
        x_i = self.x0
        if iterations is not None:
            for i in range(iterations):
                status_s.append(Status(i+1,
                                       x_i,
                                       self.f(x_i),
                                       self.df(x_i),
                                       NewtonRaphson.error(x_im1, x_i)))
                x_im1 = x_i
                x_i -= self.f(x_i) / self.df(x_i)
            return status_s
        elif tolerance is not None:
            i = 0
            tolerance = pow(10, -tolerance)
            temp_tolerance = None
            while temp_tolerance is None or temp_tolerance > tolerance:
                status_s.append(Status(i+1,
                                       x_i,
                                       self.f(x_i),
                                       self.df(x_i),
                                       NewtonRaphson.error(x_im1, x_i)))

                temp_tolerance = NewtonRaphson.error(x_im1, x_i)
                x_im1 = x_i
                x_i -= self.f(x_i) / self.df(x_i)
                i += 1
            return status_s


class A(NewtonRaphson):
    def f(self, x):
        return -(x*x) + 1.8*x + 2.5

    def df(self, x):
        return -2*x + 1.8


class B(NewtonRaphson):
    def f(self, x):
        return math.exp(-0.5*x)*(4 - x) - 2

    def df(self, x):
        return -math.exp(-0.5*x)*(4-x)*(-0.5)*math.exp(-0.5*x)


nr = A(5.0).run(tolerance=int(input('Enter Tolerance: ')))

for n in nr:
    n.print()


tolerance = int(input('Enter Tolerance: '))

try:
    nr = B(2.0).run(tolerance=tolerance)
    for n in nr:
        n.print()
except OverflowError:
    print('s')


nr = B(6.0).run(tolerance=tolerance)
for n in nr:
    n.print()


nr = B(8.0).run(tolerance=tolerance)
for n in nr:
    n.print()
