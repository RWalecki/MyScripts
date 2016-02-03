import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def table(
    ax,
    dat,
    c_range=None,
    fontsize=10,
    colorbar=True,
):

    if c_range==None:
        vmax = np.max(np.abs(dat))
        vmin = -vmax
    else:
        vmin, vmax = c_range


    im = ax.imshow(dat.T,
               interpolation='nearest',
               cmap=cm.seismic,
               vmin=vmin,
               vmax=vmax,
               )


    for (x,y),v in np.ndenumerate(dat):

        val = np.int32(v*100)/100.

        if v<=(vmax-vmin)*0.5:
            color = 'white'
        else:
            color = 'black'

        ax.text(x, y, val, va='center', ha='center',color=color,fontsize=fontsize)

    return im