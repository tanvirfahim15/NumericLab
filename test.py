digits = [str(i) for i in range(9)]
digits.append('.')
digits.append('-')


def parse_term(term):
    coefficient, var = '',''
    for char in term:
        if char not in digits:
            var += char
        elif len(var)>0:
            var += char
        else:
            coefficient += char
    if coefficient == '':
        return 1.0, var
    elif coefficient == '-':
        return -1.0, var
    return float(coefficient), var


def parse_eq(eq):
    eq = eq.replace(' ','')
    eq = eq.split('=')
    rhs = float(eq[1])
    print(rhs)
    eq = eq[0].replace('-','+-')
    eq = eq.split('+')
    for term in eq:
        if len(term) > 0:
            print(parse_term(term))
    return eq


eq = '-s-2.0a+3b-c=9'
parse_eq(eq)