#! /usr/bin/env python3

'''Navarro-Frenk-White halo model

Author: Hector Salas <hector.salas.o@gmail.com>'
'''

# ------- Imports -------

import numpy as np
import astropy.units as u

from astropy.modeling import Fittable1DModel, Parameter
from astropy.cosmology import Planck15 as cosmo

# ------- Functions -------


class NFW(Fittable1DModel):
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
    inputs = ('r',)
    outputs = ('v',)

    v200 = Parameter(bounds=(0, 200))
    c = Parameter(bounds=(1e-12, 30))
    fit_deriv = None


    @staticmethod
    def evaluate(r, v200, c):
        r = r*u.kpc
        v200 = v200*u.km/u.s
        r200 = (v200/cosmo.H0).to(u.kpc)
        # r200 = (v200/(68.0*u.km/u.s/u.Mpc)*100).to(u.kpc)
        # r200 = v200/cosmo.h*1e3
        x = r/r200
        v =  v200*np.power((np.log(1.0+c*x)-c*x/(1.0+c*x))/(x*(np.log(1.0+c)-c/(1.0+c))), 0.5)
        v = v.to(u.km/u.s)
        v = v.value
        return(v)
    #
    # @staticmethod
    # def fit_deriv(r, v200, c):
    #     r = r*u.kpc
    #     v200 = v200*u.km/u.s
    #     r200 = v200/cosmo.H0*100.
    #     x = r/r200
    #     aux1 = np.log(1.0+c*x)-c*x/(1.0+c*x)
    #     aux2 = np.log(1.0+c)-c/(1.0+c)
    #     d_v = np.power(aux1/(x*aux2), 0.5)
    #     d_c1 = v200.value*np.power(d_v,-1)*c/2.
    #     d_c2 = (x/np.power(1+c*x,2))/aux2
    #     d_c3 = aux1*(-1)/(x*np.power(aux2,2))/np.power(1+c,2)
    #     d_c = d_c1*(d_c2*d_c3)
    #     return([d_v, d_c])
