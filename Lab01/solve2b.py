
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
        ca0 = 42
        cb0 = 28
        cc0 = 4
        k = 0.016
        return ((cc0 + x) / (pow((ca0 - 2 * x), 2) * (cb0 - x))) - k

    @staticmethod
    def error(x_new, x_old):
        if x_old is None:
            return None
        return math.fabs((x_new-x_old)/x_new)

    @staticmethod
    def get_mid(x1,x2):
        return ((-FalsePosition.function(x1)*(x1-x2))/(FalsePosition.function(x1)-FalsePosition.function(x2)))+x1

    def run(self):
        new_mid = FalsePosition.get_mid(self.x_neg,self.x_pos)
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

xm, err, fxm = [], [], []


tolerance = pow(10, -int(input('Enter Tolerance:')))
print('iteration   Upper value   Lower value   Xm   f(Xm)   Relative approximate error')

temp_tolerance = None
i = 0
while temp_tolerance is None or temp_tolerance > tolerance:
    st = fp.run()
    if st.err is not None:
        print('%3d %10.5f %10.5f %10.5f %10.5f  %10.5f '%(i + 1, st.x_p, st.x_n, st.x_m, st.f_xm, st.err))
    else:
        print('%3d %10.5f %10.5f %10.5f %10.5f    -------  '%(i + 1, st.x_p, st.x_n, st.x_m, st.f_xm))
    xm.append(st.x_m)
    err.append(st.err)
    fxm.append(st.f_xm)
    temp_tolerance = st.err
    i += 1

plt.ylabel('Error')
plt.xlabel('Iteration')
plt.plot(err)
plt.savefig('fp.png')
plt.show()

