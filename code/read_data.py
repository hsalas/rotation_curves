#! /usr/bin/env python3

# Read rotation curves data from file and passes to a QTable

from astropy.table import Table, QTable
from astropy.io import ascii
import astropy.units as u

# ------- Functions -------

def read_data_file(data_file, directory):
    ''' Reads the data file containing the rotations curve of a galaxy and pass the data to a table.
    input:
        data_file: (str) Name of the file containg the rotation curve of the galaxy.
            Radius |  vgas   |  vdisk  |  vbulge |  vobs   | err vobs|   Vu    |   Vt    |   Rxv   |   Vxy   |
            kpc       km/s      km/s       km/s     km/s     km/s       km/s      km/s       kpc       km/s
    output:
        table: (QTable) Table wiht de data.
    '''

    colnames = ['radius','vgas', 'vdisk', 'vbulge', 'vobs', 'err-vobs', 'vu', 'vt', 'rxv', 'vxy']
    # dtype = [u.quantity.Quantity, u.quantity.Quantity, u.quantity.Quantity, u.quantity.Quantity, u.quantity.Quantity, u.quantity.Quantity, u.quantity.Quantity, u.quantity.Quantity, u.quantity.Quantity, u.quantity.Quantity]

    table = ascii.read(directory + data_file, names=colnames)
    table = Table(table)
    qtable = QTable()
    # table['radius'].units = u.kpc
    # table['vgas'].units = u.km/u.s
    # table['vdisk'].units = u.km/u.s
    # table['vbulge'].units = u.km/u.s
    # table['vobs'].units = u.km/u.s
    # table['err-vobs'].units = u.km/u.s
    # table['vu'].units = u.km/u.s
    # table['vt'].units = u.km/u.s
    # table['rxv'].units = u.kpc
    # table['vxy'].units = u.km/u.s
    qtable['radius'] = table['radius']*u.kpc
    qtable['vgas'] = table['vgas']*u.km/u.s
    qtable['vdisk'] = table['vdisk']*u.km/u.s
    qtable['vbulge'] = table['vbulge']*u.km/u.s
    qtable['vobs'] = table['vobs']*u.km/u.s
    qtable['err-vobs'] = table['err-vobs']*u.km/u.s
    qtable['vu'] = table['vu']*u.km/u.s
    qtable['vt'] = table['vt']*u.km/u.s
    qtable['rxv'] = table['rxv']*u.kpc
    qtable['vxy'] = table['vxy']*u.km/u.s
    # import pdb;pdb.set_trace()
    return(qtable)
