#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kplr
import numpy as np
import matplotlib.pyplot as pl
from matplotlib.ticker import MaxNLocator

client = kplr.API()
kois = client.kois(where="koi_pdisposition+like+'CANDIDATE'")
print(len(kois))
log_period = np.log10([k.koi_period for k in kois])
log_ror = np.log10([k.koi_ror for k in kois])

fig = pl.figure(figsize=(6, 6))
pl.gca().axvline(np.log10(365.), color="#cccccc", lw=3)
pl.gca().axhline(np.log10(0.009155), color="#cccccc", lw=3)
pl.plot(log_period, log_ror, ".", color="#222222", ms=5)
pl.xlim(-0.2, 2.75)
pl.ylim(-2.4, -0.7)
pl.gca().yaxis.set_major_locator(MaxNLocator(5))
pl.ylabel("$\log_{10} R_p/R_\star$")
pl.xlabel("$\log_{10} P/\mathrm{day}$")
fig.subplots_adjust(left=0.18, bottom=0.15, right=0.98, top=0.95)
pl.savefig("planet_properties.pdf")
