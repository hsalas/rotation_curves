#! /usr/bin/env python3

'''Script that reads data files with rotation curves of galaxies

Author: Hector Salas <hector.salas.o@gmail.com>'
'''

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

    table = ascii.read(directory + data_file, names=colnames)
    table = Table(table)
    qtable = QTable()
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
    return(qtable)
