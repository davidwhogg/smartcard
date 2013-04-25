#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import kplr
import numpy as np
import pyfits

# Get the planet parameters from the API.
client = kplr.API()
k10b = client.planet("10b").koi
k10c = client.planet("10c").koi

# Download the data files.
datasets = [dataset.fetch() for dataset in k10b.data]

time = np.array([])
sap = np.array([])
pdc = np.array([])
flux = np.array([])

for dataset in datasets:
    data = kplr.Dataset(dataset.filename, untrend=True, maxditer=5)
    if data.cadence:
        print(dataset.filename)
        time = np.append(time, data.time)
        sap = np.append(sap, data.sapflux / np.median(data.sapflux))
        pdc = np.append(pdc, data.pdcflux / np.median(data.pdcflux))
        flux = np.append(flux, data.flux)

pyfits.new_table(pyfits.ColDefs([pyfits.Column(name="time", format="E",
                                               array=time),
                                 pyfits.Column(name="sapflux", format="E",
                                               array=sap),
                                 pyfits.Column(name="pdcflux", format="E",
                                               array=pdc),
                                 pyfits.Column(name="flux", format="E",
                                               array=flux)])
                 ).writeto("untrend.fits", clobber=True)
