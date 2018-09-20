import numpy as np


class Equation:
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-']
    matrix = []
    equations = []

    def __init__(self,_equations):
        self.equations = _equations

    @staticmethod
    def parse_term(term):
        coefficient, var = '', ''
        for char in term:
            if char not in Equation.digits:
                var += char
            elif len(var) > 0:
                var += char
            else:
                coefficient += char
        if coefficient == '':
            return 1.0, var
        elif coefficient == '-':
            return -1.0, var
        return float(coefficient), var

    @staticmethod
    def parse_equation(equation):
        equation = equation.replace('\n', '')
        equation = equation.replace(' ', '')
        equation = equation.split('=')
        rhs = float(equation[1])
        equation = equation[0].replace('-', '+-')
        equation = equation.split('+')
        data = dict()
        for term in equation:
            if len(term) > 0:
                pair = Equation.parse_term(term)
                data[pair[1]] = pair[0]
        return data, rhs

    def get_matrix(self):
        keys = []
        matrix = []

        for equation in self.equations:
            lhs = Equation.parse_equation(equation)[0]
            for key in lhs.keys():
                if key not in keys:
                    keys.append(key)
        for equation in self.equations:
            row = []
            lhs = Equation.parse_equation(equation)[0]
            rhs = Equation.parse_equation(equation)[1]
            for key in keys:
                if key in lhs.keys():
                    row.append(lhs[key])
                else:
                    row.append(0.0)
            row.append(rhs)

            matrix.append(row)
        return np.asarray(matrix), keys
