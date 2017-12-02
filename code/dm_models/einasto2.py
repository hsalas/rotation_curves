#! /usr/bin/env python3

'''Einasto halo model

Author: Hector Salas <hector.salas.o@gmail.com>'
'''

# ------- Imports -------

import numpy as np
import astropy.units as u

from astropy.cosmology import Planck15 as cosmo
from scipy.special import gamma, gammainc
from astropy.constants import G, M_sun

# ------- Functions -------


def halo_einasto2(r, par_list):
    '''Einasto halo model
    Inputs:
        r:  array_like
            Radius in Kpc. Must be non negative.

        par_list:   list of length 3.
                    Parameters of Einasto model.
                    par_list[0]:    float or int.
                                    rho_e2  in Msol/pc3.
                    par_list[1]:    float or int.
                                    r_e2 in Kpc.
                    par_list[2]:    mu
    Outputs
        v:
            velocity in km/s.
    '''
    try:
        np.array(r, float)
    except ValueError:
        raise TypeError("type(r) must be array_like of int or float")
    if (r.all() < 0):
        raise ValueError("r values must be greater than 0")
    elif type(par_list) != list:
        raise TypeError("type(par_list) must be list")
    elif len(par_list) != 3:
        raise IndexError("len(par_list) must be 3")
    elif (type(par_list[0]) != int and type(par_list[0]) != float):
        raise TypeError("type(par_list[0]) must be int or float")
    elif (type(par_list[1]) != int and type(par_list[1]) != float):
        raise TypeError("type(par_list[1]) must be int or float")
    elif (type(par_list[2]) != int and type(par_list[2]) != float):
        raise TypeError("type(par_list[1]) must be int or float")
    elif par_list[1] == 0:
        raise ZeroDivisionError("par_list[1] must be different from 0")
    elif par_list[2] == 0:
        raise ZeroDivisionError("par_list[1] must be different from 0")

    r = r*u.kpc
    rho_e2 = par_list[0]*10**(-3)*u.M_sun/np.power(u.kpc, 3)
    r_e2 = par_list[1]*u.kpc   # rayon de densite rho2
    mu = par_list[2]
    dn = 2.0*mu
    xx = dn*np.power(r/r2, 1.0/mu)
    igma = gammainc(3*mu, xx.value)*gamma(3*mu)
    v = np.sqrt(G*4*np.pi*np.power(r2, 3)*rho2*np.power(2.0, -3.0*mu)*np.power(mu, 1.0-3*mu)*np.exp(dn)*igma/r)
    v = v.to(u.km/u.s)
    return(v)
