'''ISO halo model

Author: Hector Salas <hector.salas.o@gmail.com>'
'''

# ------- Imports -------

import numpy as np
import astropy.units as u

from astropy.constants import G, M_sun
from scipy import integrate

# ------- Functions -------


def rho(r, rho_0, rc):
    '''Function that gives mass denity of the model

        r:  array_like
            Radius in Kpc. Must be non negative
        rho_0:  float or int.
                Central mass density Rho_0  in 10^-3 Msol/pc^3.
        rc:     float or int.
                Core radius in Kpc.
    Outputs
        rho:
                mass density.
    '''
    try:
        np.array(r, float)
    except ValueError:
        raise TypeError("type(r) must be array_like of int or float")
    if (r.all() < 0):
        raise ValueError("r values must be greater than 0")
    elif (type(rho_0) != int and type(rho_0) != float):
        raise TypeError("type(par_list[0]) must be int or float")
    elif (type(rc) != int and type(rc) != float):
        raise TypeError("type(par_list[1]) must be int or float")
    elif rc == 0:
        raise ZeroDivisionError("rc must be different from 0")
    elif rho_0 < 0:
        raise ValueError("rho_0 cannot be negative")
    elif rc < 0:
        raise ValueError("rc cannot be negative")
    else:
        pass

    rho = rho_0/np.power(1.0 + np.power(r/rc,2), 1.5)*np(r*1000.0, 2)
    return(rho)

def halo_iso_0230(r, par_list):
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
    elif type(par_list) != list:
        raise TypeError("type(par_list) must be list")
    elif len(par_list) != 2:
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
    # rho = rho_0/np.power(1.0 + np.power(r/rc,2), 1.5)
    mass = [4*np.pi*integrate.romberg(rho, 0., r[i]) for i in r]
    v = np.sqrt(G*mass/r)
    return(v)
