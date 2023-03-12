from timeit import default_timer as timer
import joblib
from algorithms.sieve1 import sieve1
from algorithms.sieve2 import sieve2
from algorithms.sieve3 import sieve3
from algorithms.sieve4 import sieve4
from algorithms.sieve5 import sieve5


# 4th slowest, 3rd second slowest, 5th third slowest, 2 ,1
num = ['', 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]

algorithm = [sieve1, sieve2, sieve3, sieve4, sieve5]
results = []
for alg in range(5):
    n = 100
    results.append([])
    for i in range(9):
        n *= 2
        prime = [True] * (n + 1)
        s = timer()
        algorithm[alg](prime)
        results[alg].append(timer() - s)

for row in results:
    print(row)

joblib.dump(results, 'results.data')
