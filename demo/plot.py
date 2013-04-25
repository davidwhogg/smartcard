#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import numpy as np
import pyfits
import matplotlib.pyplot as pl
from matplotlib.ticker import MaxNLocator

with pyfits.open("untrend.fits") as f:
    data = f[1].data
    time = np.array(data["TIME"])
    sap = 1e3 * np.array(data["SAPFLUX"])
    pdc = 1e3 * np.array(data["PDCFLUX"])
    flux = 1e3 * np.array(data["FLUX"])

fig = pl.figure(figsize=[8, 8])
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

ax1.plot(time, sap - 1e3, ".k")
ax2.plot(time, pdc - 1e3, ".k")
ax3.plot(time, flux - 1e3, ".k")

std = np.std(sap[~np.isnan(sap)])
ax1.set_ylim([-5 * std, 5 * std])

std = np.std(pdc[~np.isnan(pdc)])
ax2.set_ylim([-5 * std, 5 * std])
ax3.set_ylim(ax2.get_ylim())

ax1.set_xticklabels([])
ax2.set_xticklabels([])

mn, mx = time[~np.isnan(time)].min(), time[~np.isnan(time)].max()
for ax, s in zip([ax1, ax2, ax3], ["raw", "PDC corrected", "untrended"]):
    ax.set_xlim([mn, mx])
    ax.set_ylabel(r"$\Delta\,[\times 10^{3}]$")
    ax.yaxis.set_label_coords(-0.1, 0.5)
    ax.yaxis.set_major_locator(MaxNLocator(6))
    ax.annotate(s, [1, 1], xycoords="axes fraction", ha="right", va="top",
                xytext=[-5, -5], textcoords="offset points")

ax3.set_xlabel(r"time [KBJD]")

fig.savefig("data.png")
