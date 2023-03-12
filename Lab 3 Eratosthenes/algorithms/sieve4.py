from timeit import default_timer as timer


def sieve4(c):
    n = len(c)
    c[1] = False
    i = 2
    while i < n:
        j = 2
        while j < i:
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1


prime = [True] * (25000 + 1)
s = timer()
sieve4(prime)
print(timer() - s)
