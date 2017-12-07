#! /usr/bin/env python3

'''
Script that adjust the rotation curve of a galaxy by with a dark matter halo
model.

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
import glob

# ------- Args --------

# get models in dm_models
model_list = model_handler.get_model_list(print_list='no')
model_list = str(model_list)[1:-1]

help_text = 'Fits rotation curves of a galaxy with a dark matter halo model.'
sign_off = 'Author: Hector Salas O. <hector.salas.o@gmail.com>'
parser = argparse.ArgumentParser(description=help_text, epilog=sign_off)

# user input args.
parser.add_argument('-f', '--File', type=str, default='ngc3198.dat', dest='file', metavar='FILE', help='(str) Name of file containing the rotation curve of the galaxy. Default value "ngc3198" ', action='store')
parser.add_argument('-p', '--Path', type=str, default='../data/', dest='path', metavar='PATH', help='(str) Path of dorectory containing the data files. Default value "../data/".', action='store')
parser.add_argument('-m', '--Model', type=str, default='nfw', dest='model', metavar='MODEL', help='(str) Model to fit. Available models: '+model_list+'.', action='store')
parser.add_argument('-o', '--Output', type=int, default=1, dest='output', metavar='OUTPUT', help='''Output of the results: 0 ->Save to file.
                                                1 ->Show on screen (default).''')

arguments = parser.parse_args()

# ------- Functions -------


def check_user_args(arguments, model_list):
    '''Function to check for errors user args. If no error returns the user args
    variables, otherwise it raises the corresponding errors.

    Inputs:
        arguments:  <class 'argparse.Namespace'>.
                    User args.
        model_list: str.
                    String with the list of available models.
    Outputs:
        user_args:  tuple.
                    Tuple with the user args.
                    (out, model_name, data_file, directory)
    '''
    out = arguments.output
    model_name = arguments.model
    data_file = arguments.file
    directory = arguments.path

    model_name.lower()
    if (out != 1) and (out != 0):
        raise ValueError('OUTPUT must be either 1 or 0')
    if model_name not in model_list:
        raise ValueError('''Invalid model name. Chek list of available
            models:'''+model_list)
    if not glob.os.path.isdir(directory):
        raise ValueError(f'Directory {directory} does not exists.')
    if not glob.os.path.isfile(directory+data_file):
        raise ValueError(f'File {directory}{data_file} does not exists.')
    user_args = (out, model_name, data_file, directory)
    return(user_args)


def main():
    # check if user args are velid.
    user_args = check_user_args(arguments, model_list)
    # read data.
    data = read_data.read_data(user_args[2], user_args[3])
    # call to model.
    model = model_handler.model_caller(user_args[1])
    # fit model to data.
    result = fits.fit(data, model[0])
    # plot of fitted model.
    plots.plot(data, result[0], model[1], user_args[2], show=user_args[0])
    # report of fit results.
    logs.log(user_args[2], model[1], result, show=user_args[0])

# ------------MAIN------------

if __name__ == '__main__':
    main()
