import joblib
import matplotlib.pyplot as plt

num = ['', 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400, 204800, 409600, 819200, 1638400]
r = [num, ['Heap'], ['Merge'], ['Quick'], ['Counting']]

for i in range(4):
    for j in joblib.load(f'arrays/results{i+1}.data'):
        r[i+1].append(round(j, 10))

print('\n'.join([''.join(['{:11}'.format(item) for item in row])
      for row in r]))

num = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400, 204800, 409600, 819200, 1638400]
r = []
for i in range(4):
    r.append(joblib.load(f'arrays/results{i+1}.data'))

plt.plot(num, r[0], label='Heap')
plt.ylabel('Time (s)')
plt.xlabel('Array length')
plt.show()

plt.plot(num, r[0], label='Heap')
plt.plot(num, r[1], label='Merge')
plt.ylabel('Time (s)')
plt.xlabel('Array length')
plt.legend()
plt.show()

plt.plot(num, r[0], label='Heap')
plt.plot(num, r[1], label='Merge')
plt.plot(num, r[2], label='Quick')
plt.ylabel('Time (s)')
plt.xlabel('Array length')
plt.legend()
plt.show()

plt.plot(num, r[0], label='Heap')
plt.plot(num, r[1], label='Merge')
plt.plot(num, r[2], label='Quick')
plt.plot(num, r[3], label='Counting')
plt.ylabel('Time (s)')
plt.xlabel('Array length')
plt.legend()
plt.show()
