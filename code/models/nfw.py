'''Navarro-Frenk-White halo model

Author: Hector Salas <hector.salas.o@gmail.com>'
'''

# ------- Imports -------

import numpy as np
import astropy.units as u

from astropy.cosmology import Planck15 as cosmo
from astropy.constants import G, M_sun

# ------- Functions -------


def halo_nfw(r, par_list):
    '''Navarro-Frenk-White halo model

    Inputs:
        r:  array_like.
            Radius in Kpc. Must be non negative.

        par_list:   list, of length 2, of
                    Parameters of NFW model.
                    par_list[0]:    float or int.
                                    v200  in km/s
                    par_list[1]:    float or int.
                                    concentration parameter, no units.
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
    elif len(par_list) != 2:
        raise IndexError("len(par_list) must be 2")
    elif (type(par_list[0]) != int and type(par_list[0]) != float):
        raise TypeError("type(par_list[0]) must be int or float")
    elif (type(par_list[1]) != int and type(par_list[1]) != float):
        raise TypeError("type(par_list[1]) must be int or float")
    elif par_list[0] == 0:
        raise ZeroDivisionError("par_list[0] value must be different than 0")
    else:
        pass
    v200 = par_list[0]*u.km/u.s
    c = par_list[1]
    r200 = v200/cosmo.h
    x = r/r200
    v = v200*np.power((np.log(1.0+c*x)-c*x/(1.0+c*x))/(x*(no.log(1.0+c)-c/(1.0+c))), 0.5)
    return(v)
