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


def halo_einasto(r, par_list):
    '''Einasto halo model
    Inputs:
        r:  array_like
            Radius in Kpc. Must be non negative.

        par_list:   list of length 3.
                    Parameters of Einasto model.
                    par_list[0]:    float or int.
                                    rho2  in Msol/pc3.
                    par_list[1]:    float or int.
                                    concentration parameter, no units.
                    par_list[2]:    mu
    Outputs
        v:
            velocity in km/s.
    '''

    if (type(r) != int and type(r) != float):
        raise TypeError("type(r) must be int or float")
    elif r < 0:
        raise ValueError("r value must be greater than 0")
    elif type(par) != list:
        raise TypeError("type(par_list) must be list")
    elif len(par) != 3:
        raise ValueError("len(par_list) must be 3")
    elif (type(par_list[0]) != int and type(par_list[0]) != float):
        raise TypeError("type(par_list[0]) must be int or float")
    elif (type(par_list[1]) != int and type(par_list[1]) != float):
        raise TypeError("type(par_list[1]) must be int or float")
    elif (type(par_list[2]) != int and type(par_list[2]) != float):
        raise TypeError("type(par_list[1]) must be int or float")
    elif par_list[1] == 0:
        raise ValueError("par_list[1] must be different from 0")

    rho2 = param[0]*u.M_sun/(u.kpc)**3    # densite ou la pente vaut -2 : rho2 10-3 Msol/pc3
    r2 = param[1]    # rayon de densite rho2
    mu = param[2]
    dn = 2.0*mu
    xx = dn*np.power(r/r2, 1.0/mu)
    igma = gammainc(3*mu, xx)*gamma(3*mu)
    v = sqrt(G*4*np.pi*np.power(2, 3)*rho2*np.power(2.0, -3.0*mu)*np.power(mu, 1.0-3*mu)*np.exp(dn)*igma/r)
    return(v)
