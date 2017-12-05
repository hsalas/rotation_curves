#! /usr/bin/env python3

'''Script that handles the log of the fits.
Author: Hector Salas O.
'''

# ------- Imports -------

def log(data_file, name, result,  show=1):
    '''Function that handles the log of the fit.

    Inputs:
        data_file   str.
                    Name of file with the data.
        model_name  str.
                    Name of model used in fit.
        results
                    result of the fir
        show:   int. Optional.
                If 0 log is stored in corresponfing file in the logs directory.
                If 1 log is print in screen.
    '''
    new_model = result[0]
    fit_info = result[1]
    if show:
        print(f'Fit info {data_file}, model {name}.')
        print('\n\nResulting model: \n\n', new_model)
        print('\n\nFit details:\n\n')
        for key in fit_info.keys():
            print(f'{key}\t{fit_info[key]}')
    else:
        index = data_file.index('.')
        data = data_file[:index]
        with open(f'../logs/fit_{data}_{name}.log', 'w') as f:
            f.write(f'Fit info {data_file}, model {name}.')
            f.write('\n\nResulting model: \n\n'+str(new_model))
            f.write('\n\nFit details:\n\n')
            for key in fit_info.keys():
                f.write(f'\n{key}\t{fit_info[key]}\n')
        f.close
        print(f'fit log save to fit_{data}_{name}.log in logs directory')
