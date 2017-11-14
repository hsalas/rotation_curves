'''ISO halo model

Author: Hector Salas <hector.salas.o@gmail.com>'
'''

# ------- Imports -------

import numpy as np
import astropy.units as u

from astropy.constants import G, M_sun

# ------- Functions -------


def halo_iso(r, par_list):
    '''ISO halo model
    Inputs:
        r:  array_like
            Radius in Kpc. Must be non negative.

        par_list:   list of length 3.
                    Parameters of Einasto model.
                    par_list[0]:    float or int.
                                    Central mass density Rho_0  in 10^-3 Msol/pc^3.
                    par_list[1]:    float or int.
                                    Core radius in Kpc.
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
    elif type(par) != list:
        raise TypeError("type(par_list) must be list")
    elif len(par) != 2:
        raise IndexError("len(par_list) must be 2")
    elif (type(par_list[0]) != int and type(par_list[0]) != float):
        raise TypeError("type(par_list[0]) must be int or float")
    elif (type(par_list[1]) != int and type(par_list[1]) != float):
        raise TypeError("type(par_list[1]) must be int or float")
    elif par_list[1] == 0:
        raise ZeroDivisionError("par_list[1] must be different from 0")
    elif par_listp[0] < 0:
        raise ValueError("par_list[0] cannot be negative")
    elif par_listp[1] < 0:
        raise ValueError("par_list[1] cannot be negative")
    else:
        pass

    rho_0 = param[0]*10**(-3)*u.M_sun/(u.pc)**3
    rc = par_list[1]*u.kpc
    v = np.sqrt(4*np.pi*G*rho_0*np.power(rc, 2)*(1.0-(rc/r)*np.arctan(r/rc)))
    return(v)
