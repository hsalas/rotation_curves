#! /usr/bin/env python3

'''ISO halo model

Author: Hector Salas <hector.salas.o@gmail.com>'
'''

# ------- Imports -------

import numpy as np
import astropy.units as u

from astropy.constants import G, M_sun
from astropy.modeling import Fittable1DModel, Parameter

# ------- Functions -------


class ISO(Fittable1DModel):
    '''ISO dark mater halo model
    Inputs:
        r:  array_like.
            Radius in Kpc.

        Parameters of ISO model.
        rho_0:    float or int.
            Central mass density in 10^-3 Msol/pc^3.
        rc: float or int.
            Core radius in Kpc.
    Outputs
        v:  array_like.
            velocity in km/s.
    '''
    inputs = ('r',)
    outputs = ('v',)

    rho_0 = Parameter(bounds=(1e-8, 1e3))
    rc = Parameter(bounds=(0, 300))
    fit_deriv = None

    @staticmethod
    def evaluate(r, rho_0, rc):
        '''ISO dark mater halo function.
        '''
        r = r*u.kpc
        rho_0 = rho_0*10**(-3)*u.M_sun/(u.pc)**3
        rc = rc*u.kpc
        c = (rc/r).value
        v = np.sqrt(4*np.pi*G*rho_0*np.power(rc, 2)*(1.0 - c*np.arctan(1/c)))
        v = v.to(u.km/u.s)
        v = v.value
        return(v)
