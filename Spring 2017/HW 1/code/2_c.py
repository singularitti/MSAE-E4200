#!/usr/bin/env python
"""
Problem 2(c).
"""
# -*- coding: utf-8 -*-
# created at Jan 26, 2017 23:13
# created by Nil-Zil

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import os
from numba import jit

plt.style.use("classic")

time = 50
niter = 2 ** 14  # number of iterations
t = np.linspace(0, time, num=niter, endpoint=True)
my_path = os.path.abspath(__file__ + "/../../")


class MolecularDynamics(object):

    def __init__(self, time, niter, initial_pos):
        self.position = np.zeros(niter)
        self.velocity = np.zeros(niter)
        self.energy = np.zeros(niter)
        self.x_average = np.zeros(niter)
        self.x_sum = 0  # intermediate position sum
        self.vel = 0  # intermediate variable
        self.force = 0  # intermediate variable
        self.e = 0  # intermediate energy
        self.initial_pos = initial_pos  # initial position
        self.pos = self.initial_pos
        self.time = time
        self.niter = niter
        self.time_step = self.time / self.niter
        self.mass = 1
        self.k = 1  # stiffness coefficient
        self.lamb = 1  # lambda
        self.alpha = 1  # quartic coefficient

    @jit
    def iter(self):
        for i in xrange(niter):
            # step 1 of leap frog
            self.vel += self.time_step / 2.0 * self.force / self.mass
            self.pos += self.time_step * self.vel
            # step 2 of leap frog
            self.force = - self.k * self.pos - self.lamb * \
                self.pos ** 2 - self.alpha * self.pos ** 3
            self.vel += self.time_step / 2.0 * self.force / self.mass

            # calculate energy
            self.e = 1 / 2 * self.mass * self.vel ** 2 + \
                1 / 2 * self.k * self.pos ** 2 + \
                1 / 3 * self.lamb * self.pos ** 3 + \
                1 / 4 * self.alpha * self.pos ** 4

            self.x_sum += self.pos
            self.velocity[i] = self.vel  # record vel after 1 time step
            self.position[i] = self.pos  # record pos after 1 time step
            self.energy[i] = self.e  # record e after 1 time step
            self.x_average[i] = self.x_sum / (i + 1)


@jit
def xmean_of_energy(e):
    return 4 * 1 * e / (3 * 1 * e - 4 * 1**2)  # lambda=gamma=alpha=1

mds = [MolecularDynamics(time, niter, xx) for xx in np.linspace(0, 0.5, num=500)]
[md.iter() for md in mds]  # loop to change value

# plot
fig1 = plt.figure()
ax1 = plt.gca()
ax1.plot(t, mds[-1].position, label="$x$ as a function of $t$")
ax1.plot(t, mds[-1].velocity, label="$v$ as a function of $t$")
ax1.set_xlabel("$t$", fontsize=16)
ax1.set_ylim((-1.8, 2.2))
ax1.legend(loc="best")
fig1.savefig(my_path + "/images/pro_2_c_1.pdf")

# average position as a function of energy
mds_x_avg = [md.x_average[-1] for md in mds]
mds_e = [md.e for md in mds]
ana_e = map(xmean_of_energy, mds_e)
mean_field_e = 1/3 * np.array(map(xmean_of_energy, mds_e))
e_min = min(mds_e)
e_max = max(mds_e)

fig2 = plt.figure()
ax2 = plt.gca()
ax2.plot(mds_e, mds_x_avg, label="molecular Dynamics result")
ax2.plot(mds_e, ana_e, label="analytic result")
ax2.plot(mds_e, mean_field_e, label="mean-field result")
ax2.set_xlabel("$\\varepsilon$", fontsize=16)
ax2.set_ylabel("$\\langle x \\rangle$", fontsize=16)
ax2.set_xlim((e_min, e_max))
ax2.set_title("$\\langle x \\rangle$ as a function of $\\varepsilon$")
ax2.legend(loc="best")
fig2.savefig(my_path + "/images/pro_2_c_2.pdf")

# energy and x vs t
fig3 = plt.figure()
ax3 = fig3.add_subplot(211)
ax3.plot(t, mds[-1].energy)
ax3.set_title("$\\varepsilon$ as a function of $t$")
ax3.set_xlabel("$t$", fontsize=16)
ax3.set_ylabel("$\\varepsilon$", fontsize=16)

ax4 = fig3.add_subplot(212)
ax4.plot(t, mds[-1].x_average)
ax4.set_title("$\\langle x \\rangle$ as a function of $t$")
ax4.set_xlabel("$t$", fontsize=16)
ax4.set_ylabel("$\\langle x \\rangle$", fontsize=16)

fig3.tight_layout()
fig3.savefig(my_path + "/images/pro_2_c_3.pdf")

# plt.show()
