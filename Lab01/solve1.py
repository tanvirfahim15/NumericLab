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
        if Bisection.function(0, x1)<0 < Bisection.function(0, x2):
            self.x_neg = x1
            self.x_pos = x2
        elif Bisection.function(0, x2)<0 < Bisection.function(0, x1):
            self.x_neg = x2
            self.x_pos = x1
        else:
            self.x_neg = x2
            self.x_pos = x1
            raise ValueError('No root is possible')
        self.x_mid = None

    @staticmethod
    def function(n, x):
        ans = pow(x / 2, n)
        temp = 0
        for k in range(1, 96):
            a = pow(-1, k)
            b = pow((pow(x, 2) / 4), k)
            c = math.factorial(k) * math.factorial(n + k)
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
        f_x = Bisection.function(0, self.x_mid)
        st = state(self.x_neg,self.x_pos,self.x_mid,error,f_x)
        if f_x > 0:
            self.x_pos = self.x_mid
        else:
            self.x_neg = self.x_mid
        return st


x0 = []
x1 = []
x2 = []

x=0.0
while x <= 10.0:
    x0.append(Bisection.function(0,x))
    x1.append(Bisection.function(1,x))
    x2.append(Bisection.function(2,x))
    x += 0.1

plt.ylabel('J(0,x)')
plt.xlabel('x')
plt.plot(x0)
plt.savefig('solve1/J0x.png')
plt.show()
plt.ylabel('J(1,x)')
plt.xlabel('x')
plt.plot(x1)
plt.savefig('solve1/J1x.png')
plt.show()
plt.ylabel('J(2,x)')
plt.xlabel('x')
plt.plot(x2)
plt.savefig('solve1/J2x.png')
plt.show()

print('X     f(X)')
x = 1
while x < 3.1:
    print('%2.1f  %10.8f' % (x, Bisection.function(0, x)))
    x += 0.1

print()

bs = Bisection(float(input('Enter x1: ')), float(input('Enter x2: ')))

xm, err, fxm = [], [], []

tolerance = pow(10, -int(input('Enter Tolerance:')))
print(tolerance)
temp_tolerance = None
i = 0
print('iteration   Upper value   Lower value   Xm   f(Xm)   Relative approximate error')
while temp_tolerance is None or temp_tolerance>tolerance:
    st = bs.run()
    if st.err is not None:
        print('%3d %10.5f %10.5f %10.5f %10.5f  %10.5f '%(i + 1, st.x_n, st.x_p, st.x_m, st.f_xm, st.err))
    else:
        print('%3d %10.5f %10.5f %10.5f %10.5f    -------  '%(i + 1, st.x_n, st.x_p, st.x_m, st.f_xm))

    xm.append(st.x_m)
    err.append(st.err)
    fxm.append(st.f_xm)
    temp_tolerance=st.err
    i += 1


plt.ylabel('Relative approximate error')
plt.xlabel('xm')
plt.plot(xm, err)
plt.savefig('solve1/xm vs error.png')
plt.show()
plt.clf()
plt.ylabel('Relative approximate error')
plt.xlabel('Iterations')
plt.plot(err)
plt.savefig('solve1/Iterations vs error.png')
plt.show()