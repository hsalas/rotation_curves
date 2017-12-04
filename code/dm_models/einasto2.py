#! /usr/bin/env python3

'''Einasto halo model

Author: Hector Salas <hector.salas.o@gmail.com>'
'''

# ------- Imports -------

import numpy as np
import astropy.units as u

from astropy.modeling import Fittable1DModel, Parameter
from astropy.cosmology import Planck15 as cosmo
from scipy.special import gamma, gammainc
from astropy.constants import G, M_sun

# ------- Functions -------


class halo_einasto2(Fittable1DModel):
    '''Einasto dark matter halo model
    Inputs:
        r:  array_like
            Radius in Kpc. Must be non negative.

        rho_e2: float or int.
                rho_e2  in Msol/pc3.
        r_e2:   float or int.
                r_e2 in Kpc.
        mu:     float or int.
                no units
    Outputs
        v:  array_like
            velocity in km/s.
    '''
    inputs = ('r',)
    outputs = ('v',)

    rho_e2 = Parameter(bounds=(1e-8, 1e3))
    r_e2 = Parameter(bounds=(1e-8, 300))
    mu = Parameter(bounds=(1e-8, 20))
    fit_deriv = None

    @staticmethod
    def evaluate(r, rho_e2, r_e2, mu):
        '''Einasto dark matter model function
        '''
        r = r*u.kpc
        rho_e2 = rho_e2*u.M_sun/np.power(u.pc, 3)
        r_e2 = r_e2*u.kpc   # rayon de densite rho2
        dn = 2.0*mu
        xx = dn*np.power(r/r_e2, 1.0/mu)
        igma = gammainc(3*mu, xx.value)*gamma(3*mu)
        v = np.sqrt(G*4*np.pi*np.power(r_e2, 3)*rho_e2*np.power(2.0, -3.0*mu)*np.power(mu, 1.0-3*mu)*np.exp(dn)*igma/r)
        v = v.to(u.km/u.s)
        v = v.value
        return(v)
