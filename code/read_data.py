# Read rotation curves data from file and passes to a QTable

from astropy.table import QTable
from astropy.io import ascii
import astropy.units as u

# ------- Functions -------

def read_data(data_file, directory):
    ''' Reads the data file containing the rotations curve of a galaxy and pass the data to a table.
    input:
        data_file: (str) Name of the file containg the rotation curve of the galaxy.
            Radius |  vgas   |  vdisk  |  vbulge |  vobs   | err vobs|   Vu    |   Vt    |   Rxv   |   Vxy   |
            kpc       km/s      km/s       km/s     km/s     km/s       km/s      km/s       kpc       km/s
    output:
        table: (QTable) Table wiht de data.
    '''

    colnames=['radius','vgas', 'vdisk', 'vbulge', 'vobs', 'err-vobs', 'vu', 'vt', 'rxv', 'vxy']
    table = ascii.read(directory + data_file, names=colnames)
    table = QTable(table)
    table['radius'].units = u.kpc
    table['vgas'].units = u.km/u.s
    table['vdisk'].units = u.km/u.s
    table['vbulge'].units = u.km/u.s
    table['vobs'].units = u.km/u.s
    table['err-vobs'].units = u.km/u.s
    table['vu'].units = u.km/u.s
    table['vt'].units = u.km/u.s
    table['rvx'].units = u.kpc
    table['vxy'].units = u.km/u.s
    return(table)

# ------- Main -------

if __name__ == '__main__':
