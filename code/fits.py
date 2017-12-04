#! /usr/bin/env python3

'''Script that handles the fits

Author: Hector Salas <hector.salas.o@gmail.com>'
'''

# ------- Imports -------

import numpy as np
from astropy.modeling.fitting import LevMarLSQFitter
import matplotlib.pyplot as plt

# ------- Functions -------


def fit(data, model, weights='no'):
    '''Function that fits the model to the data calling fitting method
     LevMarLSQFitter from astropy.modeling.fitting

    Inputs:
        data:   Table, QTable.
                Table with the data.
        model:  Fittable1DModel
                model to be fiitted.
        weigths:    str (yes/no). Optional.
                If set to 'yes' the erros of the data are inculded as weigths.
    '''
    x = data['radius'].value
    v_obs = np.power(data['vobs'].value, 2)
    v_gas = np.power(data['vgas'].value, 2)
    v_disk = np.power(data['vdisk'].value, 2)
    v_bulge = np.power(data['vbulge'].value, 2)
    y = v_obs - v_gas - v_disk - v_bulge
    y = np.sqrt(np.abs(y))
    pfit = LevMarLSQFitter()
    if weights == 'yes':
        err = data['err-vobs'].value
        weigths = 1/np.power(err, 2)
        new_model = pfit(model, x, y, weights=weigths)
    else:
        new_model = pfit(model, x, y, maxiter=1000)
    info = pfit.fit_info
    return(new_model, info)
