# rotation_curves

Python scripts that fits models to rotations curves of spiral galaxies by dark matter halo models.

main: rotation_curves.py 
exceute with -h or --help option to view help.

Data and otputs:

Data files should be added to the data folder.
Resulting plots if choosen to be saved (default) to file will be stored the plots folder.
Resulting log files from the fits if choosen to be saved (default) to file will be stored the plots folder.

Adding new dark matter model:

New models should be created in their own file 'new_model.py' and stored in the code/dm_models/ directory.
To create a new dark matter halo model follow the guideliines from astropy.modeling:
http://docs.astropy.org/en/stable/modeling/new.html#a-step-by-step-definition-of-a-1-d-gaussian-model
