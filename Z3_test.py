# -*- coding: utf-8 -*-
# time: 2023/9/29 18:58
# file: Z3_test.py
# author: Felix_Zhang


from z3 import *

if __name__ == '__main__':

    # x = Int('x')
    # y = Int('y')
    # print(simplify(x + y + 2 * x + 3))
    # print(simplify(x < y + x + 2))
    # print(simplify(And(x + 1 >= 3, x ** 2 + x ** 2 + y ** 2 + 2 >= 5)))
    #
    # x = Int('x')
    # y = Int('y')
    # n = x + y >= 3
    # print("num args: ", n.num_args())
    # print("children: ", n.children())
    # print("1st child:", n.arg(0))
    # print("2nd child:", n.arg(1))
    # print("operator: ", n.decl())
    # print("op name:  ", n.decl().name())

    # x = Real('x')
    # y = Real('y')
    # solve(x ** 2 + y ** 2 > 3, x ** 3 + y < 5)

    # x = Real('x')
    # y = Real('y')
    # solve(x ** 2 + y ** 2 == 3, x ** 3 == 2)
    #
    # set_option(precision=30)
    # print("Solving, and displaying result with 30 decimal places")
    # solve(x ** 2 + y ** 2 == 3, x ** 3 == 2)

    # print (1 / 3)
    # print (RealVal(1) / 3)
    # print (Q(1, 3))

    # x = Real('x')
    # solve(3 * x == 1)
    #
    # set_option(rational_to_decimal=True)
    # solve(3 * x == 1)
    #
    # set_option(precision=30)
    # solve(3 * x == 1)

    # x = Real('x')
    # solve(x > 4, x < 0)

    # Boolean Logic

    # p = Bool('p')
    # q = Bool('q')
    # r = Bool('r')
    # solve(Implies(p, q), r == Not(q), Or(Not(p), r))

    # p = Bool('p')
    # q = Bool('q')
    # print(And(p, q, True))
    # print(simplify(And(p, q, True)))
    # print(simplify(And(p, False)))

    # p = Bool('p')
    # x = Real('x')
    # solve(Or(x < 5, x > 10), Or(p, x ** 2 == 2), Not(p))

    # x = Int('x')
    # y = Int('y')
    #
    # s = Solver()
    # print(s)
    #
    # s.add(x > 10, y == x + 2)
    # print(s)
    # print("Solving constraints in the solver s ...")
    # print(s.check())
    #
    # print("Create a new scope...")
    # s.push()
    # s.add(y < 11)
    # print(s)
    # print("Solving updated set of constraints...")
    # print(s.check())
    #
    # print("Restoring state...")
    # s.pop()
    # print(s)
    # print("Solving restored set of constraints...")
    # print(s.check())

    # x = Real('x')
    # s = Solver()
    # s.add(2 ** x == 3)
    # print(s.check())

    # x = Real('x')
    # y = Real('y')
    # s = Solver()
    # s.add(x > 1, y > 1, Or(x + y > 3, x - y < 2))
    # print("asserted constraints...")
    # for c in s.assertions():
    #     print("c:" ,c)
    #
    # print(s.check())
    # print("statistics for the last check method...")
    # print(s.statistics())
    # # Traversing statistics
    # for k, v in s.statistics():
    #     print(k, " : ", v)

    # x, y, z = Reals('x y z')
    # s = Solver()
    # s.add(x > 1, y > 1, x + y > 3, z - x < 10)
    # print(s.check())
    #
    # m = s.model()
    # print("x = %s" % m[x])
    #
    # print("traversing model...")
    # for d in m.decls():
    #     print("%s = %s" % (d.name(), m[d]))
    #
    # x = Int('x')
    # y = Int('y')
    # f = Function('f', IntSort(), IntSort())
    # solve(f(f(x)) == x, f(x) == y, x != y)

    # x = Int('x')
    # y = Int('y')
    # f = Function('f', IntSort(), IntSort())
    # s = Solver()
    # s.add(f(f(x)) == x, f(x) == y, x != y)
    # print(s.check())
    # m = s.model()
    # print("f(f(x)) =", m.evaluate(f(f(x))))
    # print("f(x)    =", m.evaluate(f(x)))

    # Create list [1, ..., 5]
    # print([x + 1 for x in range(5)])
    #
    # # Create two lists containg 5 integer variables
    # X = [Int('x%s' % i) for i in range(5)]
    # Y = [Int('y%s' % i) for i in range(5)]
    # print(X)
    #
    # # Create a list containing X[i]+Y[i]
    # X_plus_Y = [X[i] + Y[i] for i in range(5)]
    # print(X_plus_Y)
    #
    # # Create a list containing X[i] > Y[i]
    # X_gt_Y = [X[i] > Y[i] for i in range(5)]
    # print(X_gt_Y)
    #
    # print(And(X_gt_Y))
    #
    # # Create a 3x3 "matrix" (list of lists) of integer variables
    # X = [[Int("x_%s_%s" % (i + 1, j + 1)) for j in range(3)]for i in range(3)]
    # pp(X)

    # X = IntVector('x', 5)
    # Y = RealVector('y', 5)
    # P = BoolVector('p', 5)
    # print(X)
    # print(Y)
    # print(P)
    # print([y ** 2 for y in Y])
    # print(Sum([y ** 2 for y in Y]))

    s = solve()









