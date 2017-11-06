from astropy.table import QTable
from astropy.io import ascii

# ------- Functions -------

def read_data(data_file):
    ''' Reads the data fro data_file and stores it in an table.
    input:
        data_file: file containing the data from rotation curves of galaxies with the following format:
            Radius |  vgas   |  vdisk  |  vbulge |  vobs   | err vobs|   Vu    |   Vt    |   Rxv   |   Vxy   |
            kpc       km/s      km/s       km/s     km/s     km/s       km/s      km/s       kpc       km/s
    output:
        table: Table wiht de data.(QTable)
    '''
    table = ascii.read('data_file')
    return(table)
