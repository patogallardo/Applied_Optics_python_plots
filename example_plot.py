import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('Agg')

plt.rcParams.update({'font.size': 18})
figparams = {
    'text.latex.preamble': r'\usepackage{mathpazo}',
    'text.usetex': True,
    'axes.labelsize': 17.,
    'xtick.labelsize': 18,
    'ytick.labelsize': 18,
    'xtick.major.pad': 3,
    'ytick.major.pad': 3,
    'figure.figsize': [5., 4.],
    'font.family': 'mathpazo',
    'legend.fontsize': 18}

plt.rcParams.update(figparams)
cs = plt.rcParams['axes.prop_cycle'].by_key()['color']

np.random.seed(1)
x = np.arange(5)
y = np.random.uniform(-1, 1, len(x))

plt.figure(layout='constrained')
plt.scatter(x, y, label='some data')
plt.xlabel('x [$\\mu m$]')
plt.ylabel('y[-]')
plt.legend()

plt.savefig('test_plot.png', dpi=200)
plt.savefig('test_plot.pdf')
