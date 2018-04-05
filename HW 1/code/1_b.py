#!/usr/bin/env python
"""
Problem 1(b).
"""
# -*- coding: utf-8 -*-
# created at Jan 26, 2017 14:43
# created by Nil-Zil

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use('classic')

temperature = np.linspace(0.1, 1, num=500)
alpha = np.array([0.5, 0.2, 0.1, 0.05, 0.02])
my_path = os.path.abspath(__file__ + "/../../")


def alpha_is_not_0(temp, alpha):
    return 2 * temp + 4 * temp / (3 * alpha * temp - 4)


def alpha_is_0(temp):
    return temp


plt.plot(temperature, alpha_is_not_0(
    temperature, alpha[0]), label=r'$\alpha=0.5$')
plt.plot(temperature, alpha_is_not_0(
    temperature, alpha[1]), label=r'$\alpha=0.2$')
plt.plot(temperature, alpha_is_not_0(
    temperature, alpha[2]), label=r'$\alpha=0.1$')
plt.plot(temperature, alpha_is_not_0(
    temperature, alpha[3]), label=r'$\alpha=0.05$')
plt.plot(temperature, alpha_is_not_0(
    temperature, alpha[4]), label=r'$\alpha=0.02$')
plt.plot(temperature, alpha_is_0(temperature), label=r'$\alpha=0$')
plt.xlabel(r'$T$', fontsize=16)
plt.ylabel(r'$\langle H \rangle$', fontsize=16)
plt.title(r'Problem 1(b): $\langle H \rangle$ as a function of $T$', fontsize=18)
plt.legend(loc="best")
# plt.show()
plt.savefig(my_path + "/images/pro_1_b.pdf")
