from astropy.table import QTable
from astropy.io import ascii

import read_data
import argparse

help_text = 'Reads data from files containing rotation curves of galaxies'
sign_off = 'Author: Hector Salas <hector.salas.o@gmail.com>'

parser = argparse.ArgumentParser(description=help_text, epilog=sign_off)

parser.add_argument('-file', '--File', type=str, default='ngc3198.dat', dest='file', metavar='FILE', help='Name of file containing the rotation curve of the galaxy.Default value "ngc3198" ',action='store')
parser.add_argument('-path', '--Path', type=str, default='../data/', dest='path', metavar='PATH', help='Path of dorectory containing the data files. Default value "../data/ .',action='store')

arguments = parser.parse_args()
data_file = arguments.file
directory = arguments.path

# ------- Functions -------


#------------MAIN------------

if __name__ == '__main__':
    data = read_data(data_file, directory)
