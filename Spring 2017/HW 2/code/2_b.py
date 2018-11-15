#!/usr/bin/env python
"""
Problem 2(b).
"""
# -*- coding: utf-8 -*-
# created at Feb 3, 2017 02:27
# created by Nil-Zil

from __future__ import division
import scipy.linalg
import matplotlib.pyplot as plt
import numpy as np
import os

plt.style.use('classic')

my_path = os.path.abspath(__file__ + "/../../")

if not os.path.exists(my_path + "/images"):
    os.makedirs(my_path + "/images")


class HarmonicOscillator(object):
    def __init__(self, mo):
        self.mo = mo

    # def construct_eig_problem(self, eta):
    #     kappa = np.array([[2, -1], [-1, 2]])
    #     M = np.array([[self.mo, 0], [0, eta * self.mo]])
    #
    #     return kappa, M
    #
    # def solve_eig_problem(self, eta):
    #     kappa, M = self.construct_eig_problem(eta)
    #     return np.sort(scipy.linalg.eigvalsh(kappa, M))[0]

    def analytic_eig(self, eta):
        return ((eta + 1 + np.sqrt(eta ** 2 - eta + 1)) / self.mo / eta,
                (eta + 1 - np.sqrt(eta ** 2 - eta + 1)) / self.mo / eta)

    def plot(self):
        eta = np.linspace(1, 10, num=500)
        vec_analytic_eig = np.vectorize(self.analytic_eig)
        ana_eigval = np.transpose(vec_analytic_eig(eta))
        plt.figure()
        plt.plot(eta, ana_eigval)
        plt.xlabel("$\\eta$", fontsize=16)
        plt.ylabel("$\\lambda$", fontsize=16)
        plt.title("2 eigenvalues as a function of $\\eta$", fontsize=18)
        # plt.show()
        plt.savefig(my_path + "/images/pro_2_b.pdf")

ho = HarmonicOscillator(1)
ho.plot()
