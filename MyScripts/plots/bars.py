import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.cm as cm
from matplotlib.dates import date2num
import datetime

def bars(
    ax,
    dat,
    xticks=None,
    width=0.1
):

    N = dat.shape[2]
    ind = np.arange(N)

    fig = plt.figure()
    ax = fig.add_subplot(111)
        
    for i_au in range(dat.shape[1]):
        for i_dset in range(dat.shape[0]):
            if np.mod(i_dset,2):
                rects1 = ax.bar(ind+i_au*width+width/2, dat[i_dset,i_au,:], width/2, color='r',alpha=1)
            else:
                rects1 = ax.bar(ind+i_au*width, dat[i_dset,i_au,:], width/2, color='b',alpha=1)

    if xticks==None:
        xticks=np.arange(dat.shape[2])

    plt.xticks(ind+width*dat.shape[1]/2, xticks)

    


    return ax
