def sieve3(c):
    n = len(c)
    c[1] = False
    i = 2
    while i < n:
        if c[i]:
            j = 2 * i
            while j < n:
                if j % i == 0:
                    c[j] = False
                j += 1
        i += 1
