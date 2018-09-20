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
        print(self.i,self.x,self.fx,self.dfx,self.err)


class NewtonRaphson:

    def __init__(self, x0):
        self.x0 = x0

    @staticmethod
    def f(x):
        return x*x*math.exp(-x)-0.5
        #return pow(x-4, 2)*(x+2)
        #return pow(x, 3) - 0.165 * pow(x, 2) + 3.993 * pow(10, -4)

    @staticmethod
    def df(x):
        return 2*x*math.exp(-x)-math.exp(-x)*x*x
        #return 2*(x-4)*(x+2)+pow(x-4, 2)
        #return 3*pow(x, 2) - 0.165 * 2 * x

    @staticmethod
    def error(x_old, x_new):
        if x_old is None or x_new is None:
            return None
        return math.fabs((x_new-x_old)/x_new)

    def run(self, iterations=None, tolerance=None):
        status_s = []
        x_im1 = None
        x_i = self.x0
        if iterations is not None:
            for i in range(iterations):
                status_s.append(Status(i+1,
                                       x_i,
                                       NewtonRaphson.f(x_i),
                                       NewtonRaphson.df(x_i),
                                       NewtonRaphson.error(x_im1, x_i)))
                x_im1 = x_i
                x_i -= NewtonRaphson.f(x_i) / NewtonRaphson.df(x_i)
            return status_s
        elif tolerance is not None:
            i = 0
            tolerance = pow(10, -tolerance)
            temp_tolerance = None
            while temp_tolerance is None or temp_tolerance > tolerance:
                status_s.append(Status(i+1,
                                       x_i,
                                       NewtonRaphson.f(x_i),
                                       NewtonRaphson.df(x_i),
                                       NewtonRaphson.error(x_im1, x_i)))

                temp_tolerance = NewtonRaphson.error(x_im1, x_i)
                x_im1 = x_i
                x_i -= NewtonRaphson.f(x_i) / NewtonRaphson.df(x_i)
                i += 1
            return status_s


nr = NewtonRaphson(-2.3).run(tolerance=4)

for n in nr:
    n.print()

nr = NewtonRaphson(0.2).run(iterations=5)

for n in nr:
    n.print()



