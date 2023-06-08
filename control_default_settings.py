import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('Agg')

cs = plt.rcParams['axes.prop_cycle'].by_key()['color']

np.random.seed(1)
x = np.arange(5)
y = np.random.uniform(-1, 1, len(x))

plt.figure(layout='constrained')
plt.scatter(x, y, label='some data')
plt.xlabel('x [$\\mu m$]')
plt.ylabel('y[-]')
plt.legend()

plt.savefig('control_plot.png', dpi=200)
plt.savefig('control_plot.pdf')
