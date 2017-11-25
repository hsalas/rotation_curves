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

def v_model(table, model, par_model):
    '''gets the velocity of the model for the observed radius.

    Inputs:
            table:  QTable, Table.
                    Table with the galaxy rotation curve.
            model:  function.
                    Model function.
            par_model:  list.
                        List with the model parameters.

    output:
            v:
                Velocity of the dark mater model.
    '''
    r = table['radius'].value
    v = model(r, par_model)
    return(v)

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
    vbulge = table['vbulge']
    vdisk = table['vdisk']
    vgas = table['vgas']
    vt = np.sqrt(np.power(vmodel,2)+np.power(vbulge,2)+np.power(vdisk,2)+np.power(vgas,2))
    return(vt)


def plot_rotation_curve(table, ax, components='yes'):
    '''Adds a scatter plot of the rotation of a galaxy to a subplot.

    inputs:
        table:   QTable, Table.
                    Table that contains the information regarding the rotacion
                    curve of a galaxy, with the correct format.

        ax:         matplotlib.axes._subplots.AxesSubplot

    output:

    '''
    ax.scatter(table['radius'], table['vobs'], marker='*', label='V')
    if components == 'yes':
        ax.plot(table['radius'], table['vgas'], ':', label='Gas')
        ax.plot(table['radius'], table['vdisk'], '--', label='Disk')
        ax.plot(table['radius'], table['vbulge'], marker='o', label='Bulge', ms=2)

#
# def plot_models(r, v, name, ax, c='g'):
#     '''Adds a scatter plot of the rotation of a galaxy to a subplot.
#
#     inputs:
#         ax:         matplotlib.axes._subplots.AxesSubplot
#
#     output:
#
#     '''
#     ax.plot(r,v, label=name)
#
#
# def plot_vtot():
#     '''Adds a line plot with the total rotation velocity of a galaxy
#      to a subplot.
#
#     inputs:
#
#         ax:         matplotlib.axes._subplots.AxesSubplot
#
#     output:
#
#     '''
#     ax.plot(r,v, label='Vtot')


def plot(rc_table, model, par_model):
    '''Creates a figure and the sublpots to it
    input:
        model:

        par_model:

        rc_table:

    output:
    '''
    model, name = model
    v = v_model(rc_table, model, par_model)
    vt = v_tot(rc_table, v)
    r = rc_table['radius']

    fig = plt.figure(figsize=(10, 10))
    # fig.suptitle(title, fontsize=12)
    ax = fig.add_subplot(111)
    ax.set_xlabel('R [Kpc]')
    ax.set_ylabel('V [Km/s]')
    ax.plot(r,v, label=name)
    ax.plot(r,vt, label='Vtot')
    plot_rotation_curve(rc_table, ax)
    # plot_models(rc_table, model, par_model, ax)
    ax.legend()
    plt.show()
