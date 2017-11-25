#! /usr/bin/env python3

'''Script thah handels the dark matter models

Author: Hector Salas <hector.salas.o@gmail.com>'
'''

# ------- Imports -------

import os
from models import *

# ------- Functions -------


def get_model_list(print_list='yes'):
    '''Returns a list of the available models

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


def model_name(model_name):
    '''Recives the name of a mode and redirects to the corresponding model function

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

    if 'nfw' in name:
        model = nfw.halo_nfw
        name = 'NFW'
    elif 'einasto' in name:
        model = einasto2.halo_einasto2
        name = 'Einasto'
    elif 'iso0230' in name:
        model = iso_0230.halo_iso_0230
        name = 'ISO0230'
    elif 'iso' in name:
        model = iso.halo_iso
        name = 'ISO'
    else:
        raise ValueError("Invalid model name. Chek list of available models")
        get_model_list()
    return((model, name))


def main():
    model = model_name('nfw')


# ------- main -------


if __name__ == '__main__':
    main()
