# important packages to import
import numpy as np              # vectors
import numpy.linalg as la       # linalg
import matplotlib as mpl
import matplotlib.pyplot as plt # plotting

# setting default matplotlib parameters
mpl.rcParams['axes.grid'] = True            # show the grid
mpl.rcParams['grid.linestyle'] = '-'
mpl.rcParams['grid.linewidth'] = 0.75
mpl.rcParams['grid.alpha'] = 0.5            # grid transparency
mpl.rcParams['axes.grid.which'] = 'both'    # show both major and minor axes
mpl.rcParams['xtick.minor.visible'] = True
mpl.rcParams['ytick.minor.visible'] = True
mpl.rcParams['figure.figsize'] = (6.4, 4.8) # default figure size
