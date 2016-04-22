import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.cm as cm
from matplotlib.dates import date2num
import matplotlib.cm as cm
import datetime

def side_by_side(
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

def stacked(
        ax,
        dat,
        xticks=None,
        cmap = cm.Greys
):
    percentages = (np.int16(dat/dat.sum(0)*1000))/10.
    y_pos = np.arange(len(xticks))
    N = dat.shape[0]


    patch_handles = []
    left = np.zeros(len(xticks)) # left alignment of data starts at zero
    for i, d in enumerate(dat):
        patch_handles.append(ax.barh(y_pos, d, color=cmap(i/float(N-1)), align='center', left=left))
        left += d

    # go through all of the bar segments and annotate
    for j in xrange(len(patch_handles)):
        for i, patch in enumerate(patch_handles[j].get_children()):
            bl = patch.get_xy()
            x = 0.5*patch.get_width() + bl[0]
            y = 0.5*patch.get_height() + bl[1]
            if j<N/2:c='k'
            else:c='w'
            ax.text(x,y, percentages[j,i], ha='center',va='center',color=c,fontsize=15)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(xticks)
    return ax
