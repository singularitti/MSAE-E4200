#!/usr/bin/env python3
# created at Oct 9, 2017 2:30 PM by Nil-Zil

import numpy as np
import matplotlib.pyplot as plt

gamma = np.linspace(4, 30, 500)
w0 = 2


def tau(g):
    return 1 / (gamma / 2 - np.sqrt(gamma**2 / 4 - w0**2))


fig, ax = plt.subplots()
ax.plot(gamma, tau(gamma))
ax.set_xlim((gamma[0], gamma[-1]))
ax.set_xlabel("$\\gamma$", fontsize=12)
ax.set_ylabel("$\\tau$", fontsize=12)
fig.savefig("tau.pdf")
plt.show()
