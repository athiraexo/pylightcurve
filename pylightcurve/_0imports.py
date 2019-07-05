from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import warnings
warnings.filterwarnings("ignore",
                        message='Matplotlib is building the font cache using fc-list. This may take a moment.')
warnings.filterwarnings("ignore",
                        message='The installed version of numexpr 2.4.4 is not supported in pandas and will be not be used')
warnings.filterwarnings("ignore",
                        message='\'second\' was found  to be \'60.0\', which is not in range [0,60). '
                                'Treating as 0 sec, +1 min [astropy.coordinates.angle_utilities]')

import os
import sys

if sys.version_info[0] > 2:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve
    input = raw_input

import matplotlib
if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using non-interactive Agg backend')
    matplotlib.use('Agg')
else:
    matplotlib.use('TkAgg')

import os
import sys
import glob
import gzip
import time
import emcee
import numpy as np
import scipy
import pickle
import shutil
import socket
import exodata
import exodata.astroquantities as aq
import datetime
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from scipy.interpolate import griddata
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy import interpolate
from astropy.io import fits as pf
from astropy.time import Time as astrotime
from astropy.coordinates import get_sun as astrosun
from sklearn.decomposition import FastICA, PCA
from matplotlib import rc

if int(matplotlib.__version__[0]) < 3:
    import seaborn
    seaborn.reset_orig()
