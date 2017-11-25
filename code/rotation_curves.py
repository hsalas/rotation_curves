#! /usr/bin/env python3

'''
Script that adjust the rotation curve of a galaxy by with a dark matter halo model.

Author: Hector Salas O.
'''

# ------- Imports -------

from astropy.table import QTable
from astropy.io import ascii

import plots
import model_handler
import read_data
import argparse

# ------- Args --------

help_text = 'Reads data from files containing rotation curves of galaxies'
sign_off = 'Author: Hector Salas <hector.salas.o@gmail.com>'

parser = argparse.ArgumentParser(description=help_text, epilog=sign_off)

parser.add_argument('-f', '--File', type=str, default='ngc3198.dat', dest='file', metavar='FILE', help='Name of file containing the rotation curve of the galaxy. Default value "ngc3198" ', action='store')
parser.add_argument('-p', '--Path', type=str, default='../data/', dest='path', metavar='PATH', help='Path of dorectory containing the data files. Default value "../data/ .', action='store')
parser.add_argument('-m', '--Model', type=str, default='nfw', dest='model', metavar='MODEL', help='''Model to fit.
Available models:   NFW
                    ISO
                    ISO0230
                    Einasto
''', action='store')


arguments = parser.parse_args()
data_file = arguments.file
directory = arguments.path
model_name = arguments.model

# ------- Functions -------


def v_tot(table, model):
    pass


def main():
    data = read_data.read_data(data_file, directory)
    model = model_handler.model_name(model_name)
    # import pdb;pdb.set_trace()
    plots.plot(data, model, [100, 100])


# ------------MAIN------------

if __name__ == '__main__':
    main()
