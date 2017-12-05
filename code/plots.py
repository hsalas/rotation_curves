#! /usr/bin/env python3

'''Script that handles all the plots

Author: Hector Salas O.
'''

import numpy as np
import importlib.machinery
import matplotlib.pyplot as plt

# try:
#     loader = importlib.machinery.SourceFileLoader('report', '~/python/xkcd_color/xkcd_rgb.py')
#     xkcd = loader.load_module('report')
#     color_list = xkcd.xkcd_color_code_list()
# except:


def v_tot(table, vmodel):
    '''Gives the total velocity as:
    Vt = sqrt( Vdisk^2 + Vbulge^2 + Vgas^2 + Vmodel^2)

    Inputs:
            table:  QTable, Table.
                    Table with the galaxy rotation curve.

            vmodel:
                    Velovity for the model.
    Outputs:
            vt:
                Total velocity of the galaxy.

    '''
    vbulge = np.power(table['vbulge'].value, 2)
    vdisk = np.power(table['vdisk'].value, 2)
    vgas = np.power(table['vgas'].value, 2)
    vmodel = np.power(vmodel, 2)
    vt = np.sqrt(vmodel+vbulge+vdisk+vgas)
    # import pdb; pdb.set_trace()
    return(vt)


def plot_rotation_curve(table, ax, components='no', error='no', **kwargs):
    '''Adds a scatter plot of the rotation of a galaxy to a subplot.

    inputs:
        table:   QTable, Table.
                    Table that contains the information regarding the rotacion
                    curve of a galaxy, with the correct format.

        ax:         matplotlib.axes._subplots.AxesSubplot
        components:  str (yes/no) optional.
                    if set to yes the components of the rotation curve are
                    ploted. Default = 'no'
        error:      str (yes/no) optional.
                    if set to yes the errorbars of the rotation curve are
                    ploted. Default = 'no'
    output:

    '''
    r = table['radius']
    if components == 'yes':
        ax.plot(r, table['vgas'], ':', label='Gas')
        ax.plot(r, table['vdisk'], '--', label='Disk')
        ax.plot(r, table['vbulge'], marker='o', label='Bulge', ms=2)
    if error == 'yes':
        ax.errorbar(r.value, table['vobs'].value, table['err-vobs'].value, marker='*', ls='None', **kwargs)
    else:
        ax.scatter(r, table['vobs'], marker='*', label='V', **kwargs)

def plot(rc_table, model, name, show=1, **kwargs):
    '''Creates a figure and the sublpots to it
    input:
        model:

        par_model:

        rc_table:

    output:
    '''
    r = rc_table['radius'].value
    v = model(r)
    vt = v_tot(rc_table, v)

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.set_xlabel('R [Kpc]')
    ax.set_ylabel('V [Km/s]')
    ax.plot(r,v, label=name)
    ax.plot(r,vt, label='Vtot')
    plot_rotation_curve(rc_table, ax, components='yes', **kwargs)
    ax.legend()
    if show:
        plt.show()
    else:
        plt.savefig('../plots/fit_'+name+'.pdf')
