from astropy.table import QTable
from astropy.io import ascii

# ------- Functions -------

def read_data(galaxy_name):
    ''' Reads the data file containing the rotations curve of a galaxy and pass the data to a table.
    input:
        galaxy_name: (str) Name of the galaxy whose rotationcurve data is store in the file ../data/galaxy_name.dat with the followig format:
            Radius |  vgas   |  vdisk  |  vbulge |  vobs   | err vobs|   Vu    |   Vt    |   Rxv   |   Vxy   |
            kpc       km/s      km/s       km/s     km/s     km/s       km/s      km/s       kpc       km/s
    output:
        table: (QTable) Table wiht de data.
    '''

    colnames=['radius','vgas', 'vdisk', 'vbulge', 'vobs', 'err-vobs', 'vu', 'vt', 'rxv', 'vxy']
    table = ascii.read('../data/'+galaxy_name+'.dat', names=colnames)
    table = QTable(table)
    return(table)
