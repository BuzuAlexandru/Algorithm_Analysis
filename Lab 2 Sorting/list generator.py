import numpy as np
import joblib

n = 100
for i in range(15):
    print(n)
    # lst = list(np.random.randint(low=0, high=n, size=n))
    # joblib.dump(lst, f'arrays/list{i + 1}.data')
    n *= 2

