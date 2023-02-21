import joblib
from timeit import default_timer as timer
from algorithms.heap import heapSort
from algorithms.merge import mergeSort
from algorithms.quick import quickSort
from algorithms.counting import countSort
import sys

print(sys.setrecursionlimit(2000))


def exec_time(f, n):
    s = timer()
    if f == 0:
        heapSort(n)
    elif f == 1:
        mergeSort(n)
    elif f == 2:
        quickSort(n)
    elif f == 3:
        countSort(n)
    e = timer()
    return e - s


results = []
for i in range(15):
    print(i+1)
    ar = joblib.load(f'arrays/list{i+1}.data')
    # results.append(exec_time(0, ar))
    # results.append(exec_time(1, ar))
    # results.append(exec_time(2, ar))
    results.append(exec_time(3, ar))
print(results)
joblib.dump(results, 'arrays/results4.data')
