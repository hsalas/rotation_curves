'''ISO halo model

Author: Hector Salas <hector.salas.o@gmail.com>'
'''

# ------- Imports -------

import numpy as np
import astropy.units as u

from astropy.modeling import Fittable1DModel, Parameter
from astropy.constants import G, M_sun
from scipy.integrate import romberg

# ------- Functions -------


class halo_iso_0230(Fittable1DModel):
    '''ISO0230 dark matter halo.
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
    inputs = ('r',)
    outputs = ('v',)

    rho_0 = Parameter(bounds=(1e-8, 1e3))
    rc = Parameter(bounds=(1e-12, 300))
    fit_deriv = None

    @staticmethod
    def evaluate(r, rho_0, rc):
        '''ISO0230 dark matter halo function
        '''
        r = r*u.kpc
        rho_0 = rho_0*10**(-3)*u.M_sun/(u.pc**3)
        rho_0 = rho_0.to(u.M_sun/(u.kpc**3))
        rc = rc*u.kpc
        rho_0 = rho_0/np.power(1.0+np.power(r/rc, 2), 1.5)
        dr = [r[i]-r[i-1] for i in range(len(r))]
        dr[0] = r[0]
        mass = [(rho_0[i]*r[i]*r[i]*dr[i]).value for i in range(len(r))]
        mass = 4*np.pi*np.cumsum(mass)*u.M_sun
        v = np.sqrt(G*mass/r)
        v = v.to(u.km/u.s)
        v = v.value
        return(v)
