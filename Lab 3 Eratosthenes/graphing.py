import joblib
import matplotlib.pyplot as plt

num = ['', 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]
r = [num, ['Algorithm 1'], ['Algorithm 2'], ['Algorithm 3'], ['Algorithm 4'], ['Algorithm 5']]
results = joblib.load('results.data')

for i in range(5):
    for j in results[i]:
        r[i+1].append(round(j, 10))

print('\n'.join([''.join(['{:12}'.format(item) for item in row])
      for row in r]))

num = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]
r = results

plt.plot(num, r[0], label='Alg 1')
plt.plot(num, r[1], label='Alg 2')
plt.plot(num, r[2], label='Alg 3')
plt.plot(num, r[3], label='Alg 4')
plt.plot(num, r[4], label='Alg 5')
plt.ylabel('Time (s)')
plt.xlabel('Array length')
plt.legend()
plt.show()
