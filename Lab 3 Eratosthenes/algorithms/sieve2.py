def sieve2(c):
    n = len(c) - 1
    c[1] = False
    i = 2
    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j += i
        i += 1
