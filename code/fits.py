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
        model:  astropy.modeling.Fittable1DModel
                model to be fiitted.
        weigths:    str (yes/no). Optional.
                If set to 'yes' the erros of the data are inculded as weigths.
    Output:
        new_model:  astropy.modeling.Fittable1DModel
                    A copy of the input model with parameters set by the fitter.
        info:       dict.
                    Dictionary with the information from the LevMarLSQFitter and
                    the calculated chi-squared.
                    The information from LevMarLSQFitter contains the values
                    returned by scipy.optimize.leastsq see documentation at:
                    https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.leastsq.html#scipy.optimize.leastsq.

    '''
    # from the data we define the x and y vector to be fitted.
    x = data['radius'].value
    v_obs = np.power(data['vobs'].value, 2)
    v_gas = np.power(data['vgas'].value, 2)
    v_disk = np.power(data['vdisk'].value, 2)
    v_bulge = np.power(data['vbulge'].value, 2)
    y = v_obs - v_gas - v_disk - v_bulge
    y = np.sqrt(np.abs(y))
    # call an instance of the fitter
    pfit = LevMarLSQFitter()
    if weights == 'yes':#errors included in the fit
        err = data['err-vobs'].value
        weigths = 1/np.power(err, 2)
        new_model = pfit(model, x, y, weights=weigths)
    else:# errors not included in the fit
        new_model = pfit(model, x, y, maxiter=1000)
    info = pfit.fit_info
    # from the results of the fit now we calculate the chi-square values.
    N = len(data)
    n = len(model.parameters)
    s_sq = (info['fvec']**2).sum()/ (N-n)
    info['chi_sqr'] = s_sq
    return(new_model, info)
