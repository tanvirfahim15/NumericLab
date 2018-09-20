import math
import matplotlib.pyplot as plt


class Status:
    def __init__(self,i, x, x_i_m_1, fx, dfx, err):
        self.i = i
        self.x = x
        self.x_i_m_1 = x_i_m_1
        self.fx = fx
        self.dfx = dfx
        self.err = err

    def print(self):
        print("    {0:02}    ".format(self.i), "   {0:.4f}".format(self.x_i_m_1),"   {0:.4f}".format(self.x),
              "   {0:.5f}".format(self.fx), "   {0:.4f}   ".format(self.dfx), self.err)


class SecantMethod:

    def __init__(self, x0, x1):
        self.x0 = x0
        self.x1 = x1

    @staticmethod
    def f(x):
        return 8*math.sin(x)*math.exp(-x)-1

    @staticmethod
    def df(x_i_m_1, x_i):
        return (SecantMethod.f(x_i)-SecantMethod.f(x_i_m_1))/(x_i-x_i_m_1)

    @staticmethod
    def error(x_old, x_new):
        if x_old is None or x_new is None:
            return None
        return math.fabs((x_new-x_old)/x_new)

    def run(self, iterations=None, tolerance=None):
        status_s = []
        x_im1 = self.x0
        x_i = self.x1
        if iterations is not None:
            for i in range(iterations):
                status = Status(i + 1,
                                x_i,
                                x_im1,
                                SecantMethod.f(x_i),
                                SecantMethod.df(x_im1, x_i),
                                SecantMethod.error(x_im1, x_i))
                status_s.append(status)
                temp = SecantMethod.f(x_i) / SecantMethod.df(x_im1,x_i)
                x_im1 = x_i
                x_i -= temp
            return status_s
        elif tolerance is not None:
            i = 0
            tolerance = pow(10, -tolerance)
            temp_tolerance = None
            while temp_tolerance is None or temp_tolerance > tolerance:
                status = Status(i + 1,
                                x_i,
                                x_im1,
                                SecantMethod.f(x_i),
                                SecantMethod.df(x_im1, x_i),
                                SecantMethod.error(x_im1, x_i))
                status_s.append(status)
                temp_tolerance = SecantMethod.error(x_im1, x_i)

                temp = SecantMethod.f(x_i) / SecantMethod.df(x_im1, x_i)
                x_im1 = x_i
                x_i -= temp
                i += 1
            return status_s


sc = SecantMethod(0.5, 0.4).run(tolerance=int(input('Enter Tolerance: ')))
solve = 0.0
print('iteration      x(i-1)     xi       f(xi)     f’(xi)     Relative approximate error')
for n in sc:
    n.print()
    solve = n.x

print("Solution: ", solve)

