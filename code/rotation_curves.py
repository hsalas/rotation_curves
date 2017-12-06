#! /usr/bin/env python3

'''
Script that adjust the rotation curve of a galaxy by with a dark matter halo model.

Author: Hector Salas O.
'''

# ------- Imports -------

from astropy.table import QTable
from astropy.io import ascii

import model_handler
import read_data
import argparse
import plots
import fits
import logs

# ------- Args --------

#get models in dm_models
model_list = model_handler.get_model_list()

help_text = 'Fits rotation curves of a galaxy with a dark matter halo model.'
sign_off = 'Author: Hector Salas O. <hector.salas.o@gmail.com>'

parser = argparse.ArgumentParser(description=help_text, epilog=sign_off)

parser.add_argument('-f', '--File', type=str, default='ngc3198.dat', dest='file', metavar='FILE', help='(str) Name of file containing the rotation curve of the galaxy. Default value "ngc3198" ', action='store')
parser.add_argument('-p', '--Path', type=str, default='../data/', dest='path', metavar='PATH', help='(str) Path of dorectory containing the data files. Default value "../data/".', action='store')
parser.add_argument('-m', '--Model', type=str, default='nfw', dest='model', metavar='MODEL', help='''(str) Model to fit.
Available models: '''+str(model_list)[1:-1]+'.', action='store')
parser.add_argument('-o', '--Output', type=int, default=2, dest='output', metavar='OUTPUT', help='''Output of the results: 0 ->Save to file.
                                                1 ->Show on screen (default).''')

arguments = parser.parse_args()
data_file = arguments.file
directory = arguments.path
model_name = arguments.model
out = arguments.output

# ------- Functions -------


def main():
    #read data.
    data = read_data.read_data(data_file, directory)
    #call to model.
    model = model_handler.model_caller(model_name)
    #fit model to data.
    result = fits.fit(data, model[0])
    #plot of fitted model.
    plots.plot(data, result[0], model[1], data_file, show=out)
    #report of fit results.
    logs.log(data_file, model[1], result, show=out)

# ------------MAIN------------

if __name__ == '__main__':
    main()
