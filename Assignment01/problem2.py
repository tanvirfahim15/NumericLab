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
        print("    {0:02}    ".format(self.i), "   {0:.4f}".format(self.x), "   {0:.5f}".format(self.fx),
              "   {0:.4f}   ".format(self.dfx), self.err)


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
                try:
                    x_i -= self.f(x_i) / self.df(x_i)
                except ZeroDivisionError:
                    print('Derivative Zero Exception')
                    return status_s
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
        return -0.5*math.exp(-0.5*x)*(4-x)-math.exp(-0.5*x)


solve = 0.0
print('Problem 2(a)')
nr = A(5.0).run(tolerance=int(input('Enter Tolerance: ')))
print('iteration       xi       f(xi)     f’(xi)     Relative approximate error')
for n in nr:
    n.print()
    solve = n.x
print("Solution: ", solve)
print()
print('Problem 2(b)')
tolerance = int(input('Enter Tolerance: '))

print('Initial Guess: 2.0')
print('iteration       xi       f(xi)     f’(xi)     Relative approximate error')
nr = B(2.0).run(tolerance=tolerance)
for n in nr:
    n.print()
    solve = n.x
print("Solution: ", solve)
input('Press [ENTER] to continue\n')
print('Initial Guess: 6.0')
print('iteration       xi       f(xi)     f’(xi)     Relative approximate error')
nr = B(6.0).run(tolerance=tolerance)
for n in nr:
    n.print()
    solve = n.x
print("Solution: ", solve)
input('Press [ENTER] to continue\n')
print('Initial Guess: 8.0')
print('iteration       xi       f(xi)     f’(xi)     Relative approximate error')
nr = B(8.0).run(tolerance=tolerance)
for n in nr:
    n.print()
    solve = n.x
print("Solution: ", solve)