from decimal import Decimal
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import numpy as np
from numpy.linalg import matrix_power

# l1 = [5, 7, 10, 12, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
l1 = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 33, 35, 37, 39, 40]
l2 = [521, 643, 788, 1000, 1265, 1576, 2000, 2517, 3000, 4000, 5000, 6300, 7950, 10000, 12500, 15850]
r1 = []
r2 = []


def fib1_recursion(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1_recursion(n - 1) + fib1_recursion(n - 2)


def fib2_dp(n):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


def fib3_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_prev = 0
        fib = 1
        for i in range(2, n + 1):
            fib_prev, fib = fib, fib + fib_prev
        return fib


def fib4_optimized_dp(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b


def fib5_matrix(n):
    i = np.array([[0, 1], [1, 1]])
    return np.matmul(matrix_power(i, n), np.array([1, 0]))[1]


def fib6_golden_ratio(n):
    phi = Decimal((1 + 5 ** .5) / 2)
    psi = Decimal((1 - 5 ** .5) / 2)
    return (phi ** n - psi ** n) / Decimal(5 ** .5)


def exec_time(f, n):
    s = timer()
    if f == 0:
        r = fib1_recursion(n)
    elif f == 1:
        r = fib2_dp(n)
    elif f == 2:
        r = fib3_iterative(n)
    elif f == 3:
        r = fib4_optimized_dp(n)
    elif f == 4:
        r = fib5_matrix(n)
    elif f == 5:
        r = fib6_golden_ratio(n)
    e = timer()
    return e - s


def alg_name(k):
    if k == 0:
        return 'Recursion'
    elif k == 1:
        return 'DP'
    elif k == 2:
        return 'Iterative'
    elif k == 3:
        return 'Optim. DP'
    elif k == 4:
        return 'Matrix exp.'
    elif k == 5:
        return 'Binet'


for v in range(1, 6):
    r1.append([])
    for x in l1:
        if type(x) is not str:
            r1[v-1].append(round(exec_time(v, x), 10))

for v in range(1, 6):
    r2.append([])
    for x in l2:
        if type(x) is not str:
            r2[v-1].append(round(exec_time(v, x), 10))

print()
print('\n'.join([''.join(['{:11}'.format(item) for item in row])
      for row in r1]))

print()
print()

print('\n'.join([''.join(['{:11}'.format(item) for item in row])
      for row in r2]))

# plt.plot(l1, r1[0], label='Recursive')
plt.plot(l1, r1[0], label='DP')
plt.plot(l1, r1[1], label='Iterative')
plt.plot(l1, r1[2], label='Optimized DP')
plt.plot(l1, r1[3], label='Matrix exponentiation')
plt.plot(l1, r1[4], label='Binet formula')
plt.ylabel('Time (s)')
plt.xlabel('nth Fibonacci number')
plt.legend()
plt.show()
