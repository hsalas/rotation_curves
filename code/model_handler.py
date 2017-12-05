#! /usr/bin/env python3

'''Script thah handles the dark matter models.

    To add a new model create the file new_model.py in dm_models containing the
    model. To define the model follow the examples fromm:

                http://docs.astropy.org/en/stable/modeling/new.html

    The model_caller function must be updated to include the call to new_model.

Author: Hector Salas <hector.salas.o@gmail.com>'
'''

# ------- Imports -------

import os
from dm_models import *

# ------- Functions -------


def get_model_list(print_list='yes'):
    '''Returns a list of the available models.

    Inputs:
        print_list: str (yes/no). Optional.
                    If yes the list is print on scress.
                    Defaul = 'yes'
    Outputs:
        list:   list.
                list of available models.
    '''
    model_list = os.listdir('dm_models/')
    model_list
    model_list = [a[:-3] for a in model_list if ('.py' in a)]
    model_list.remove('__init__')

    if print_list == 'yes':
        print('Available models:')
        for i in model_list:
            print(i)
    return(model_list)


def model_caller(model_name):
    '''Recives the name of a model and calls an instance of the model class.

    input:
            model:  str.
                    name of the model.
    output:
            model:  tuple, (model, name).
                        model: Module with the model function.
                        name: str with model name

            name:   str.
                    String with model name in prefered format.
    '''
    name = model_name.lower()

    # Call to new models should be added here as an elif.
    if 'nfw' in name:
        model = nfw.NFW(1.,1.)
        name = 'NFW'
    elif 'einasto' in name:
        model = einasto2.EINASTO2(1.,1.,1.)
        name = 'Einasto'
    elif 'iso0230' in name:
        model = iso_0230.ISO_0230(1.,1.)
        name = 'ISO0230'
    elif 'iso' in name:
        model = iso.ISO(1.,1.)
        name = 'ISO'
    else:
        raise ValueError("Invalid model name. Chek list of available models")
        get_model_list()
    return((model, name))
